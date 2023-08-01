from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Dictionary to store registered users (this is for demonstration purposes only, use a database in production)
users = {}

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')
    name = data.get('name')
    password = data.get('password')

    if email and phone and name and password:
        # In a real application, you would want to handle duplicate registrations and password hashing securely
        user_id = str(uuid.uuid4())  # Generate a random user ID (this is for demonstration purposes only)
        users[user_id] = {
            'email': email,
            'phone': phone,
            'name': name,
            'password': password
        }
        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    else:
        return jsonify({"error": "Invalid data. Make sure to provide email, phone, name, and password."}), 400
    


# Endpoint to authenticate a user
@app.route('/login', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email and password:
        for user_id, user_info in users.items():
            if user_info['email'] == email and user_info['password'] == password:
                return jsonify({"message": "Authentication successful", "user_id": user_id}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    else:
        return jsonify({"error": "Invalid data. Make sure to provide email and password."}), 400

# Endpoint to update user information (requires authentication)
@app.route('/update', methods=['POST'])
def update_user():
    data = request.get_json()
    user_id = data.get('user_id')
    token = data.get('token')

    if user_id and token:
        if user_id in users:
            user_info = users[user_id]
            user_info['email'] = data.get('email', user_info['email'])
            user_info['phone'] = data.get('phone', user_info['phone'])
            user_info['name'] = data.get('name', user_info['name'])
            return jsonify({"message": "User information updated successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Invalid data. Make sure to provide user_id and token."}), 400

# Endpoint to log out the user (requires authentication)
@app.route('/logout', methods=['POST'])
def logout_user():
    data = request.get_json()
    user_id = data.get('user_id')
    token = data.get('token')

    # In a real application, you would invalidate the token or session associated with the user
    return jsonify({"message": "User logged out successfully"}), 200

if __name__ == "__main__":
    port_number = 20030

    print("Running on port check it out:")
    
    app.run(host='0.0.0.0', port=port_number)
