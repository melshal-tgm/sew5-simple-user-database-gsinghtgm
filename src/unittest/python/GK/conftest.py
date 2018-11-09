import pytest

from server.server import app as create_app

@pytest.fixture
def client():
    create_app.testing = True
    client = create_app.test_client()
    yield client