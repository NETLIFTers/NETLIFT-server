from init import init

users = init()


class User():
    
    _profile = { }
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
        self.lifts = []
        self.weights = []

    @property
    def programs(self):
        return self.programs

    @programs.setter
    def programs(self,new_program):
        self._programs = new_program


    @property
    def unit(self):
        return self.unit

    @property
    def active_program_id(self):
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
