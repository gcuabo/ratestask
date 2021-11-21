import pytest


@pytest.fixture
def client(app):
    app.config["TESTING"] = True
    return app.test_client()
