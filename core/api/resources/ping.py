from datetime import datetime

from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return {"pong": str(datetime.now())}
