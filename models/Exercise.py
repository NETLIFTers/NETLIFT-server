import requests
from init import exercises
exercises = exercises()


class Exercise():

    exerciseList = []

    # def getData(self):
    #     url = "https://exercisedb.p.rapidapi.com/exercises"

    #     headers = {
    #         "X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
    #         "X-RapidAPI-Key": "64cae58b9fmsh642244495256bd2p192147jsnc26154d01ade"
    #     }

    #     response = requests.request("GET", url, headers=headers)

    #     data = response.json()

    #     for exercise in data:
    #         exerciseObject = {}
    #         exerciseObject['id'] = exercise['id']
    #         exerciseObject['name'] = exercise['name']
    #         exerciseObject['bodyPart'] = exercise['bodyPart']
    #         exerciseObject['target'] = exercise['target']
    #         exerciseObject['equipment'] = exercise['equipment']
    #         exerciseObject['gifUrl'] = exercise['gifUrl']
    #         exercises.insert_one(exerciseObject)

    def find_by_bodyPart(bodyPart):
        result = exercises.find({"bodyPart": {"$regex": f"{bodyPart}"}})
        return result

    def find_by_equipment(equipment):
        result = exercises.find({"equipment": equipment})
        return result

    def find_by_target(target):
        result = exercises.find({"target": target})
        return result

    def find_by_name(name):
        result = exercises.find({"name": {"$regex": f"{name}"}})
        return result
