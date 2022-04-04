from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
import hashlib
import datetime
from init import init
from models.User import User
app = Flask(__name__)
CORS(app)
users = init()

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

programs = [
{
"id": 1,
"training_days": [1, 1, 0, 1, 1, 1, 0],
"workouts": [1, 2, 1, 5], 
}
],

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
    print(users)
    new_user = request.get_json()
    new_user['password'] = hashlib.sha224(
        new_user["password"].encode("utf-8")).hexdigest()
    users_db = users.find_one({"username": new_user["username"]})

    if not users_db:
        users.insert_one(new_user)
        return jsonify({'msg': 'User has been '}), 201
    else:
        return jsonify({'msg': 'Username already exists'}), 409


@app.route('/login', methods=['POST'])
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
    print(current_user)
    user_profile = User.find_by_name(current_user)
    return jsonify(user_profile), 200


# create program username/program

@app.route('/user/program', methods=["GET", "POST"])
def create_program():
    if request.method == "GET":
      return jsonify(programs), 200
    elif request.method == "POST":
      new_program = request.json
      last_id = programs[-1]["id"]
      new_program["id"] = last_id + 1
      users.append(new_program)
      return "New program was created", 201

@app.route('/user/program/<int:program_id>', methods=["PATCH"])
def update_program():
    

# @app.route('/user/all', methods=['GET'])
# def profile():
#     user_profile = User.getAll()
#     return jsonify({'profile': user_profile}), 200


if __name__ == "__main__":
    app.run(debug=True)

# user/userid/programs
