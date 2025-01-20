from src.db import db_obj
import bcrypt
from flask import session
from uuid import uuid4

# register a User
def register(formData):
    name = formData.get("name")
    email = formData.get("email")
    password = formData.get("password")
    address = formData.get("address")
    user_id = str(uuid4())
    
    if name and email and password and address:
        if db_obj['users'].find_one({"email": email}):
            return {"status": "error", "message": "Email already exists"}
        else:
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            db_obj['users'].insert_one(
                {
                    "uuid": user_id,
                    "name": name,
                    "email": email,
                    "password": hashed_password.decode('utf-8'),
                    "address": address,
                }
            )
            return {"status": "success", "message": "User registered successfully"}
    else:
        return {"status": "error", "message": "Please fill all the fields"}
    

# login function
def login(formData):
    email = formData.get("email")
    password = formData.get("password")

    if email and password:
        user = db_obj['users'].find_one({"email": email})
        if user:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                session['user_id'] = user['uuid']
                session['name'] = user['name']
                return {"status": "success", "message": "User logged in successfully"}
            else:
                return {"status": "error", "message": "Invalid password"}
        else:
            return {"status": "error", "message": "User not found"}
    else:
        return {"status": "error", "message": "Please fill all the fields"}
    

# find user details
def find_user_details(user_id):
    user = db_obj['users'].find_one({"uuid": user_id})
    if user:
        return {"status": "success", "data": user}
        return {"status": "success", "data": user}
    else:
        return {"status": "error", "message": "User not found"}