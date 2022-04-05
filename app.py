from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
import hashlib
import datetime
from models.User import User
# from models.Exercise import Exercise
# exercise = Exercise()

app = Flask(__name__)
CORS(app)

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
    new_user = request.get_json()
    new_user['password_digest'] = hashlib.sha224(
        new_user['password'].encode("utf-8")).hexdigest()
    user = User.find_by_name(new_user["username"])
    if not user:
        user = User.create_user(new_user)
        return (user.__dict__), 201
    else:
        return jsonify({'msg': 'Username already exists'}), 409


@app.route('/login', methods=['POST'])
def login():
    login_details = request.get_json()
    user = User.find_by_name(login_details['username'])
    if user:
        encrypted_password = hashlib.sha224(
            login_details['password'].encode("utf-8")).hexdigest()
        if encrypted_password == user['password_digest']:
            access_token = create_access_token(identity=user['username'])
            return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'The username or password is incorrect'}), 401


@app.route('/user', methods=['GET', 'POST'])
@jwt_required()
def profile():
    if request.method == "GET":
        current_user = get_jwt_identity()
        user_profile = User.find_by_name(current_user)
        return jsonify(user_profile), 200
    elif request.method == "POST":
        pass


@app.route('/programs', methods=["GET", "POST"])
@jwt_required()
def create_program():
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_program = user_profile["_programs"]
        return jsonify(user_program), 200
    elif request.method == "POST":
        new_program = request.get_json()
        program = User.add_program(current_user, new_program)
        return jsonify(program), 201


@app.route('/workouts', methods=["GET", "POST"])
@jwt_required()
def workout():
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_workout = user_profile["_workouts"]
        return jsonify(user_workout), 200
    elif request.method == "POST":
        new_workout = request.get_json()
        workout = User.add_workout(current_user, new_workout)
        return jsonify(workout), 201


# change to /program/programId
# @app.route('/program/<int:program_id>', methods=["GET", "PATCH"])
# def update_program(program_id):
#     resp = request.get_json()
#     training_days = resp[0]
#     workouts = resp[1]
#     response = users.programs.update_one(
#         {"program_id": program_id},
#         {"$set": {"training_days": training_days, "workouts": workouts}}
#     )
#     print(response.raw_result)
#     return response.raw_result, 200


# return all programs

# @app.route('/program', methods=['GET'])
# def profile():
#     user_profile = User.getAll()
#     return jsonify({'profile': user_profile}), 200

# add workouts
# add lifts

# edit workouts
# edit lifts


if __name__ == "__main__":
    app.run(debug=True)
