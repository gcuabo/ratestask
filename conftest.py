import os

import pytest

from tests.fixtures import *  # isort:skip # noqa: F403, F401


@pytest.fixture(scope="session")
def app(request):
    os.environ["FLASK_ENV"] = "testing"
    from core.application import create_flask_app

    app = create_flask_app()
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    return app
