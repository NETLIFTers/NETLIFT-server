
from tokenize import String
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
import hashlib
import datetime
from models.User import User
from models.Exercise import Exercise
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
        return (user), 201
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


@app.route('/program', methods=["GET", "POST"])
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

# change to /program/programId
@app.route('/program/<int:program_id>', methods=["GET", "PATCH"])
@jwt_required()
def update_program(program_id):
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_program = user_profile["_programs"]
        for key, val in user_program[0].items():
            print(key, val)
            # for key in i.keys():
            #     print(key)
            # if i['id'] == program_id:
            #     user_program = i
            #     print(user_program)
        return jsonify(user_program), 200
    elif request.method == "PATCH":
        changed_program = request.get_json()
        program = User.add_program(current_user, changed_program)
        return jsonify(program), 201

@app.route('/program/<int:program_id>', methods=["GET", "PATCH"])
@jwt_required()
def update_program(program_id):
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_program = user_profile["_programs"]
        for i in user_program:
            if i['id'] == program_id:
                return jsonify(i), 200
        return "Program not found", 404
    elif request.method == "PATCH":
        changed_program = request.get_json()
        program = User.update_program(
            current_user, changed_program, program_id)
        return jsonify(program), 200


@app.route('/workout', methods=["GET", "POST"])
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



@app.route('/workout/<int:workout_id>', methods=["GET", "PATCH"])
@jwt_required()
def update_workout(workout_id):
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_program = user_profile["_workouts"]
        for i in user_program:
            if i['id'] == workout_id:
                return jsonify(i), 200
        return "Workout not found", 404
    elif request.method == "PATCH":
        changed_workout = request.get_json()
        workout = User.update_program(
            current_user, changed_workout, workout_id)
        return jsonify(workout), 200


@app.route('/lift', methods=["GET", "POST"])
@jwt_required()
def create_lifts():
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_lift = user_profile["_lifts"]
        return jsonify(user_lift), 200
    elif request.method == "POST":
        new_lift = request.get_json()
        lift = User.add_lift(current_user, new_lift)
        # print(lift)
        return jsonify(lift), 201


@app.route('/lift/<int:lift_id>', methods=["GET", "PATCH"])
@jwt_required()
def update_lift(lift_id):
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_program = user_profile["_lifts"]
        for i in user_program:
            if i['id'] == lift_id:
                return jsonify(i), 200
        return "Lift not found", 404
    elif request.method == "PATCH":
        changed_lift = request.get_json()
        lift = User.update_program(
            current_user, changed_lift, lift_id)
        return jsonify(lift), 200


@app.route('/weight', methods=["GET", "POST"])
@jwt_required()
def create_weights():
    current_user = get_jwt_identity()
    user_profile = User.find_by_name(current_user)
    if request.method == "GET":
        user_weight = user_profile["_weights"]
        return jsonify(user_weight), 200
    elif request.method == "POST":
        new_weight = request.get_json()
        weight = User.add_weight(current_user, new_weight)
        return jsonify(weight), 201

# need to finish


@app.route('/exercises')
def get_exercises():
    args = request.args
    response = []
    for key in args.keys():
        terms = args[key].split(",")
        match key:
            case "bodyPart":
                print(terms)
                for term in terms:
                    result = Exercise.find_by_bodyPart(term)
                    for x in result:
                        del x['_id']
                        response.append(x)
                return (f"{response}"), 200
            case "equipment":
                pass
            case "target":
                pass
            case _:
                return "error: request not valid"

    return ("Failed"), 400

# return all programs
# @app.route('/program', methods=['GET'])
# def profile():
#     user_profile = User.getAll()
#     return jsonify({'profile': user_profile}), 200


if __name__ == "__main__":
    app.run(debug=True)
