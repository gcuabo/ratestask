import os


class Config(object):
    def __init__(self, flask_env):
        # ENVIRONMENT
        self.FLASK_ENV = flask_env
        self.DEBUG = os.environ.get("DEBUG", False)
        self.PROPAGATE_EXCEPTIONS = True

        # DATABASE
        self.DB_NAME = os.environ.get("DB_NAME") or "postgres"
        self.DB_USER = os.environ.get("DB_USER") or "postgres"
        self.DB_HOST = os.environ.get("DB_HOST") or "localhost"
        self.DB_PASSWORD = os.environ.get("DB_PASSWORD") or "postgres"
