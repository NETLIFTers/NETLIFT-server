
import json
from wsgiref import headers 
test_user = {
    "username": "test99",
    "email": "tets@gamil.com",
    "password": "11111111",
    "body_weight": 95,
    "unit": "kg",
    "smallest_increment": 1.25}

mock_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTE4MDY4NywianRpIjoiMjg1NzJiZDgtZDVjYy00OWNmLWJjMTQtZjQ2ZDcyZTJjYTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3Q5OSIsIm5iZiI6MTY0OTE4MDY4NywiZXhwIjoxNjQ5MjY3MDg3fQ.mILx-yW3p4qa5nJ4nWl1sOc-vKcF0P-8GQnf53zE_eI"
def test_api(client):
    """Initial / route works and sends back hello world"""
    res = client.get('/')
    assert res.status == "200 OK"
    assert b'Hello, World!' in res.data

def test_user_registration(client):
    """user should succesfully register"""
    mock_data = json.dumps(test_user)
    res = client.post('/register', data=mock_data, headers = {'Content-Type': 'application/json'})
    assert res.status == "409 CONFLICT"
    
def test_login(client):
    """test /login is succesfull"""
    mock_data = json.dumps(test_user)
    res = client.post('/login', data=mock_data, headers = {'Content-Type': 'application/json'})
    assert res.status == "200 OK"

# class testing_protected_routes:

    


