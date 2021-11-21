import os


class Config(object):
    def __init__(self, flask_env):
        # ENVIRONMENT
        self.FLASK_ENV = flask_env

        # DATABASE
        self.DB_NAME = os.getenv("DB_NAME") or "postgres"
        self.DB_USER = os.getenv("DB_USER") or "postgres"
        self.DB_HOST = os.getenv("DB_HOST") or "localhost"
        self.DB_PASSWORD = os.getenv("DB_PASSWORD") or "postgres"
