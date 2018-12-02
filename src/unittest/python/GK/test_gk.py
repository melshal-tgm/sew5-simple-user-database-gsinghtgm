import json

def test_show_users(client):
    rv = client.get('/users')
    assert b'{"users":{"user1":{"email":"gsingh@student.tgm.ac.at","picture":"imgur.com/321","username":"gsingh"},"user2":{"email":"gsingh2@student.tgm.ac.at","picture":"imgur.com/222","username":"gsingh2"},"user3":{"email":"gsingh3@student.tgm.ac.at","picture":"imgur.com/333","username":"gsingh3"},"user4":{"email":"gsingh3@student.tgm.ac.at","picture":"imgur.com/4444","username":"gsingh4"}}}\n' in rv.data

def test_show_user(client):
    rv = client.get('/users/user1')
    assert b'{"user1":{"email":"gsingh@student.tgm.ac.at","picture":"imgur.com/321","username":"gsingh"}}\n' in rv.data

def test_add_user(client):
    client.post('/users', json={'username': 'gsingh5', 'email': 'gsinghmail', 'picture':'gsinghpic'})
    rv = client.get('/users/user5')
    assert b'{"user5":{"email":"gsinghmail","picture":"gsinghpic","username":"gsingh5"}}\n' in rv.data

def test_update_user(client):
    client.put('/users/user5',json={'username': 'gsingh5', 'email': 'gsinghmail', 'picture':'gsinghpicnew'})
    rv=client.get('/users/user5')
    assert b'{"user5":{"email":"gsinghmail","picture":"gsinghpicnew","username":"gsingh5"}}\n' in rv.data

def test_delete_user(client):
    client.delete('/users/user5')
    rv=client.get('/users/user5')
    assert b'{"message": "User user5 doesn\'t exist.' in rv.data