import json
mock_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTE4MDY4NywianRpIjoiMjg1NzJiZDgtZDVjYy00OWNmLWJjMTQtZjQ2ZDcyZTJjYTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3Q5OSIsIm5iZiI6MTY0OTE4MDY4NywiZXhwIjoxNjQ5MjY3MDg3fQ.mILx-yW3p4qa5nJ4nWl1sOc-vKcF0P-8GQnf53zE_eI"

mock_program = json.dumps({"id": 1,"training_days": [1, 1, 0, 1, 1, 1, 0],"workouts": [1, 2, 1, 5]})

mock_workout = json.dumps({"id": 3,"lifts": [1, 2, 4],"completed": [1648727486]})

def test_user(client):
    """test /user gets 200 and returns correct user"""
    
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/user', content_type='application/json', headers = headers)
    assert res.status == "200 OK"
    assert res.json['username'] == 'test99'


def test_program(client):
    """test /program gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/program', content_type='application/json', headers = headers)
    assert res.status == "200 OK"
    res = client.post('/program', content_type='application/json', data=mock_program, headers = headers)
    assert res.status == "201 CREATED"

def test_workout(client):
    """test /workouts gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/workouts', content_type='application/json', headers = headers)
    assert res.status == "200 OK"
    res = client.post('/workouts', content_type='application/json', data=mock_workout, headers = headers)
    assert res.status == "201 CREATED"
