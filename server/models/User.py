from init import init

users = init()


class User():
    def __init__(self, data):
        self.username = data['username']
        self.email = data['email']
        self.password_digst = data['password_digest']
        self.active_program_id = 0
        self.body_weight = data['body_weight']
        self.unit = data['unit']
        self.smallest_increment = data['smallest_increment']
        self.programs = [{}]
        self.workouts = [{}]
        self.lifts = [{}]
        self.weights = [{}]

    @property
    def programs(self):
        return self.programs

    @property
    def unit(self):
        return self.unit

    @property
    def active(self):
        return self.active_program_id

    @property
    def workouts(self):
        return self.workouts

    @classmethod
    def find_by_name(self, name):
        user_profile = users.find_one({'username': name})
        # delete data we don't want to return
        del user_profile['_id'], user_profile['password']
        return user_profile

    @classmethod
    def getAll(self):
        userList = users.find_one()
        del userList['_id']
        return userList
