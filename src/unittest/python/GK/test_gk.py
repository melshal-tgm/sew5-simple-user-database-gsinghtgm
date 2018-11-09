import json

def test_show_users(client):
    rv = client.get('/users')
    assert b'{"user1": {"username": "gsingh", "email": "gsingh@student.tgm.ac.at", "picture": "imgur.com/321"}, "user2": {"username": "gsingh2", "email": "gsingh2@student.tgm.ac.at", "picture": "imgur.com/222"}, "user3": {"username": "gsingh3", "email": "gsingh3@student.tgm.ac.at", "picture": "imgur.com/333"}, "user4": {"username": "gsingh4", "email": "gsingh3@student.tgm.ac.at", "picture": "imgur.com/4444"}}' in rv.data

def test_show_user(client):
    rv = client.get('/users/user1')
    assert b'{"username": "gsingh", "email": "gsingh@student.tgm.ac.at", "picture": "imgur.com/321"}\n' in rv.data

def test_add_user(client):
    client.post('/users', json={'username': 'gsingh5', 'email': 'gsinghmail', 'picture':'gsinghpic'})
    rv = client.get('/users/user5')
    assert b'{"username": "gsingh5", "email": "gsinghmail", "picture": "gsinghpic"}\n' in rv.data

def test_update_user(client):
    client.put('/users/user5',json={'username': 'gsingh5', 'email': 'gsinghmail', 'picture':'gsinghpicnew'})
    rv=client.get('/users/user5')
    assert b'{"username": "gsingh5", "email": "gsinghmail", "picture": "gsinghpicnew"}\n' in rv.data

def test_delete_user(client):
    client.delete('/users/user5')
    rv=client.get('/users/user5')
    assert b'{"message": "User user5 doesn\'t exist.' in rv.data