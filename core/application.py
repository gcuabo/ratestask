import os
from flask import Flask
from flask_restful import Api

from .config import Config
from .exceptions import configure_exception_handler
from .urls import register_api_urls
from .db import db


def create_flask_app():
    app = Flask(__name__)

    # Get the run time env
    run_time_env = os.environ.get("FLASK_ENV", "development")

    # Configure from config file
    app.config.from_object(Config(run_time_env))

    # Setup flask restful
    api = Api(app)
    register_api_urls(api)

    # Configure Exceptions
    configure_exception_handler(app)

    # Database
    app.db = db

    return app
