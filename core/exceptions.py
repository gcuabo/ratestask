from flask import jsonify

from marshmallow.exceptions import ValidationError


def configure_exception_handler(app):
    @app.errorhandler(ValidationError)
    def marshmallow_exception_handler(e):
        status_code = 400
        response = jsonify(
            {"message": e.normalized_messages(), "status_code": status_code}
        )
        return response, status_code

    @app.errorhandler(Exception)
    def app_exception_handler(e):
        status_code = e.status_code if getattr(e, "status_code", None) else 400
        response = jsonify(
            {"message": "Bad Request: {}".format(e), "status_code": status_code}
        )

        response.status_code = status_code
        return response, status_code


class BaseException(Exception):
    message = "Internal Server Error"
    status_code = 500

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.__repr__()


class InvalidDateFromDateToException(BaseException):
    message = "Invalid 'date from' and 'date to' combination"
    status_code = 400


class InvalidOriginDestinationException(BaseException):
    message = "Origin must not be the same as Destination"
    status_code = 400


class PortOrRegionNotFound(BaseException):
    message = "Port or Region '{}' not found."
    status_code = 400

    def __init__(self, code_or_slug: str = ""):
        self.message = self.message.format(code_or_slug)
