from server.serverwithoutsqlite import create_app
from flask import url_for
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app

def test_app(client):
    assert client.get(url_for('user1')).status_code == 200