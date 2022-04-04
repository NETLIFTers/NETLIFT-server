from crypt import methods
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from pymongo import MongoClient
import hashlib
import datetime
from init import db
app = Flask(__name__)
CORS(app)

client = MongoClient(
    "mongodb+srv://netlifters:qdfoR8T7tHob6rQj@netlift.mvruz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['netLift']

users = db['users']
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/user/register', methods=['POST'])
def register():
    new_user = request.get_json()
    print(new_user, "line 30")
    new_user['password'] = hashlib.sha224(
        new_user["password"].encode("utf-8")).hexdigest()
    users_db = users.find_one({"username": new_user["username"]})

    if not users_db:
        users.insert_one(new_user)
        return jsonify({'msg': 'User has been '}), 201
    else:
        return jsonify({'msg': 'Username already exists'}), 409


@app.route('/user/login', methods=['POST'])
def login():
    login_details = request.get_json()
    user = users.find_one({'username': login_details['username']})
    if user:
        encrypted_password = hashlib.sha224(
            login_details['password'].encode("utf-8")).hexdigest()
        if encrypted_password == user['password']:
            access_token = create_access_token(identity=user['username'])
            print(access_token)
            return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'The username or password is incorrect'}), 401


@app.route('/user', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    print(current_user, "from line 61")
    user_profile = users.find_one({'username': current_user})
    print(user_profile, "form line 63")
    if user_profile:
        # delete data we don't want to return
        del user_profile['_id'], user_profile['password']
        return jsonify({'profile': user_profile}), 200
    else:
        return jsonify({'msg': 'Profile not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
