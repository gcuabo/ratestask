import os
import tests

from tests.fixtures import *  # isort:skip # noqa: F403, F401


@tests.fixture(scope="session")
def app(request):
    os.environ["FLASK_ENV"] = "testing"
    from core.application import create_flask_app

    app = create_flask_app()

    return app
