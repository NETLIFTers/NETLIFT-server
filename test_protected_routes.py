
mock_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTE4MDY4NywianRpIjoiMjg1NzJiZDgtZDVjYy00OWNmLWJjMTQtZjQ2ZDcyZTJjYTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3Q5OSIsIm5iZiI6MTY0OTE4MDY4NywiZXhwIjoxNjQ5MjY3MDg3fQ.mILx-yW3p4qa5nJ4nWl1sOc-vKcF0P-8GQnf53zE_eI"

def test_user(client):
    """test /user gets 200 and returns correct user"""
    
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/user', content_type='application/json', headers = headers)
    assert res.status == "200 OK"
    assert res.json['username'] == 'test99'


def test_get_program(client):
    """test /program gets 200 and returns correct user"""
    headers = {'Authorization': 'Bearer {}'.format(mock_token)}
    res = client.get('/program', content_type='application/json', headers = headers)
    assert res.status == "200 OK"
