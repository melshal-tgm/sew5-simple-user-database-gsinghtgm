import json
import pytest
from server.serverwithoutsqlite import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def test_post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='users')


def test_json_of_response(response):
    return json.loads(response.data.decode('utf8'))