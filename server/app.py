from flask import Flask, render_template, request, jsonify
from init import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


users = [
  {'id':1, 'username': 'Falcon', 'program': 'A'},
  {'id':2, 'username': 'Owl', 'program': 'B'},
  {'id':3, 'username': 'Parrot', 'program': 'C'}
]
programs = [
{
"id": 1,
"training_days": [1, 1, 0, 1, 1, 1, 0],
"workouts": [1, 2, 1, 5], 
}
],

@app.route('/')
def home():
    return "<h1>Welome to NetLift<h1>"

# all user data plus create user

@app.route('/users', methods=["GET", "POST"])
def show_users():
    if request.method == "GET":
      return jsonify(users), 200
    elif request.method == "POST":
      new_user = request.json
      last_id = users[-1]["id"]
      new_user["id"] = last_id + 1
      users.append(new_user)
      return f"{new_user['username']} was created", 201


# show specific user

@app.route('/users/<string:username>')
def show_user(username):
    try:
        return next(user for user in users if user["username"] == username), 200
    except:
        raise BadRequest(f"Cant't find user with that name: {username}")

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



if __name__ == "__main__":
    app.run(debug=True)
