import time
from flask import Flask,request,jsonify
from flask_pymongo import MongoClient
import os

app = Flask(name)

try: 
   mongo =MongoClient(os.environ.get('mongodb://127.0.0.1:27017/db'))
   db=mongo.get_database("Training")
   print("db is connected!.")
except:
    print("db is not connected!..")

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    users_collection = db.users
    exist_user = users_collection.find_one({"username":username})
    print(f'{exist_user}')
    if exist_user and exist_user.get("password") == password:    
        return jsonify({"message":"user was login sucessfully!!..","id":str(exist_user.get("_id"))}),201, {"Content-Type": "application/json"}
    return jsonify({"message":"user was not found!!.."}),400, {"Content-Type": "application/json"}

        
@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    print(f'{data} json')
    username = data.get("username")
    password = data.get("password")
    users_collection = db.users
    exist_user = users_collection.find_one({"username": username})
    if exist_user:
        return jsonify({"message":"email is already register!.."}),400, {"Content-Type": "application/json"}
    new_user = users_collection.insert_one({"username":username,"password":password})
    print(f'{new_user} new user')
    return jsonify({"message":"user was created sucessfully!!..","id":str(new_user.inserted_id)}),201, {"Content-Type": "application/json"}

if name == "main":
    app.run(debug=True)
    "proxy": "http://localhost:5000",