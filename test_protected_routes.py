import json
mock_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTI3NDU4NSwianRpIjoiOGFmMWU0NDAtMjM3OC00YjllLTg3ZDktOTIzYTcyYTVkYzA4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3Q5OSIsIm5iZiI6MTY0OTI3NDU4NSwiZXhwIjoxNjQ5MzYwOTg1fQ.DJQTfiYoghat2LVg3szwcchT-YwHxrOfqZDSnUyW3Tk"

mock_program = json.dumps(
    {"id": 1, "training_days": [1, 1, 0, 1, 1, 1, 0], "workouts": [1, 2, 1, 5]})

mock_workout = json.dumps(
    {"id": 3, "lifts": [1, 2, 4], "completed": [1648727486]})

mock_lifts = json.dumps(
    {"id": 3, "name": "squat", "reps": 5, "sets": 5, "exercise_id": 1})

mock_updated_lifts = json.dumps(
    {"id": 3, "name": "squat", "reps": 5, "sets": 8, "exercise_id": 1})

mock_weights = json.dumps(
    {"user_id": 1, "lift_id": 3, "history": [60, 90, 80]})


def test_user(client):
    """test /user gets 200 and returns correct user"""

    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/user', content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    assert res.json['username'] == 'test99'


def test_program(client):
    """test /program gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get(
        '/program', content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    res = client.post('/program', content_type='application/json',
                      data=mock_program, headers=headers)
    assert res.status == "201 CREATED"


def test_workout(client):
    """test /workouts gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get(
        '/workout', content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    res = client.post('/workout', content_type='application/json',
                      data=mock_workout, headers=headers)
    assert res.status == "201 CREATED"


def test_lifts(client):
    """test /lift gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/lift', content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    res = client.post('/lift', content_type='application/json',
                      data=mock_lifts, headers=headers)
    assert res.status == "201 CREATED"


def test_lift_id(client):
    """test lift/id returns lift"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get(
        "/lift/3", content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    res = client.patch(
        "/lift/3", content_type='application/json', data=mock_updated_lifts, headers=headers)
    assert res.status == "200 OK"


def test_weights(client):
    """test /weight gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get(
        '/weight', content_type='application/json', headers=headers)
    assert res.status == "200 OK"
    res = client.post('/weight', content_type='application/json',
                      data=mock_weights, headers=headers)
    assert res.status == "201 CREATED"


def test_user_deletion(client):
    """user should be deleted"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.delete('/user', content_type='application/json',
                        headers=headers)
    assert res.status == "200 OK"
