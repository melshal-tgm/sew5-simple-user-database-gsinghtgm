import pytest

from server.serverwithoutsqlite import app as create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app