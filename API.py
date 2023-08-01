from flask import Flask, request, jsonify

app = Flask(__name__)

# Sampling user data 
users = []

# Endpoint to register a new user
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')
    name = data.get('name')
    password = data.get('password')

    # Check if the required fields are provided
    if not email or not phone or not name or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    # Check if the user already exists (based on email or phone)
    if any(user['email'] == email or user['phone'] == phone for user in users):
        return jsonify({'message': 'User already exists'}), 409

    new_user = {
        'email': email,
        'phone': phone,
        'name': name,
        'password': password
    }
    users.append(new_user)

    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint to authenticate a user
@app.route('/api/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user based on the provided email
    user = next((user for user in users if user['email'] == email), None)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Authentication successful'}), 200

# Endpoint to update user information
@app.route('/api/update', methods=['PUT'])
def update_user():
    data = request.get_json()
    token = data.get('token')  # Assuming the token is generated during login

    # Find the user based on the provided token
    user = next((user for user in users if user.get('token') == token), None)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Update user information
    user['email'] = data.get('email', user['email'])
    user['phone'] = data.get('phone', user['phone'])
    user['name'] = data.get('name', user['name'])

    return jsonify({'message': 'User information updated successfully'}), 200

# Endpoint to log out the user (clear token)
@app.route('/api/logout', methods=['POST'])
def logout_user():
    data = request.get_json()
    token = data.get('token')

    # Find the user based on the provided token
    user = next((user for user in users if user.get('token') == token), None)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Clear the token (log out the user)
    user['token'] = None

    return jsonify({'message': 'User logged out successfully'}), 200

if __name__ == '__main__':
    port_number = 444

    print("Running on port check it out:")
    
    app.run(host='0.0.0.0', port=port_number)
