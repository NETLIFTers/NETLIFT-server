from types import NoneType
from init import init
from pymongo import ReturnDocument
users = init()


class User():

    def __init__(self, data):
        self.username = data["username"]
        self.email = data["email"]
        self.password_digest = data["password_digest"]
        self._active_program_id = 0
        self.body_weight = data["body_weight"]
        self._unit = data["unit"]
        self.smallest_increment = data["smallest_increment"]
        self._programs = []
        self._workouts = []
        self._lifts = []
        self._weights = []

    @property
    def programs(self):
        return self._programs

    @programs.setter
    def programs(self, new_program):
        self._programs.append(new_program)

    @property
    def workouts(self):
        return self.workouts

    @workouts.setter
    def workouts(self, new_workout):
        self._workouts.append(new_workout)

    @property
    def lifts(self):
        return self.lifts

    @lifts.setter
    def lifts(self, new_lifts):
        self._lifts.append(new_lifts)

    @property
    def weights(self):
        return self.weights

    @weights.setter
    def weights(self, weights):
        self._weights.append(weights)

    @property
    def unit(self):
        return self.unit

    @unit.setter
    def unit(self, new_unit):
        self._unit = new_unit

    @property
    def active_program_id(self):
        return self.active_program_id

    @active_program_id.setter
    def active_program_id(self, new_id):
        self._active_program_id = new_id

    @classmethod
    def find_by_name(self, name):
        user_profile = users.find_one({'username': name})
        # delete data we don't want to return
        if user_profile:
            del user_profile['_id']
        return user_profile

    @classmethod
    def get_all(self):
        userList = users.find_one()
        del userList['_id']
        return userList

    @classmethod
    def add_program(self, username, new_program):
        print(new_program)
        updated_program = users.find_one_and_update({'username': username}, {
            "$push": {'_programs': new_program}}, return_document=ReturnDocument.AFTER)
        return updated_program['_programs']

    
    @classmethod
    def update_program(self, username, update_program):
        print(update_program)
        changed_program = users.find_one_and_update({'username': username}, {
            "$set": {'_programs': update_program}}, return_document=ReturnDocument.AFTER)
        return changed_program['_programs']

    @classmethod
    def add_lift(self, username, new_lift):
        # print(new_program)
        updated_lift = users.find_one_and_update({'username': username}, {
            "$push": {'_lifts': new_lift}}, return_document=ReturnDocument.AFTER)
        return updated_lift['_lifts']

    @classmethod
    def add_weight(self, username, new_weight):
        # print(new_program)
        updated_weight = users.find_one_and_update({'username': username}, {
            "$push": {'_weights': new_weight}}, return_document=ReturnDocument.AFTER)
        return updated_weight['_weights']
    
    @classmethod
    def add_workout(self, username, new_workout):
        updated_program = users.find_one_and_update({'username': username}, {
            "$push": {'_workouts': new_workout}}, return_document=ReturnDocument.AFTER)
        return updated_program['_workouts']

    @classmethod
    def create_user(self, data):
        user = User(data)
        userData = {}
        for key, value in (user.__dict__.items()):
            userData[key] = value
        users.insert_one(userData)
        return user
