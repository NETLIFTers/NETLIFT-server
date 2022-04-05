from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://netlifters:qdfoR8T7tHob6rQj@netlift.mvruz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['netLift']


def users():
    users = db['users']
    return users


def exercises():

    exercises = db['exercises']
    return exercises
