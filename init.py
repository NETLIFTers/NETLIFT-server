from pymongo import MongoClient


def init():
    client = MongoClient(
        "mongodb+srv://netlifters:qdfoR8T7tHob6rQj@netlift.mvruz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['netLift']
    users = db['users']
    return users
