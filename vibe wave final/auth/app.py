from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from database import users_collection
import os

app = Flask(__name__)
CORS(app)

# ✅ Serve Static Files (HTML, CSS, JS)
@app.route("/")
def serve_home():
    return send_from_directory(".", "login.html")

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(".", filename)

# ✅ Signup Route
@app.route("/auth/signup", methods=["POST"])
def signup():
    data = request.json
    name, email, password = data["name"], data["email"], data["password"]

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"name": name, "email": email, "password": hashed_password})
    
    return jsonify({"message": "Signup successful"}), 201

# ✅ Login Route
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    email, password = data["email"], data["password"]

    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
