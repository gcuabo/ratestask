from marshmallow import Schema, fields, validates_schema, validates

from core.exceptions import (
    InvalidDateFromDateToException,
    PortOrRegionNotFound,
    InvalidOriginDestinationException,
)
from core.models.port import Port
from core.models.region import Region

date_format = "%Y-%m-%d"


class RatesGetInputSchema(Schema):
    """ /rates GET

    Parameters:
        - date_from (date)
        - date_to (date)
        - origin (str)
        - destination (str)
    """

    date_from = fields.Date(required=True, format=date_format)
    date_to = fields.Date(required=True, format=date_format)
    origin = fields.String(required=True)
    destination = fields.String(required=True)

    @validates_schema
    def validate_dates(self, data, **kwargs):
        date_from = data.get("date_from")
        date_to = data.get("date_to")

        if date_to < date_from:
            raise InvalidDateFromDateToException()

        data["date_from"] = date_from.strftime(date_format)
        data["date_to"] = date_to.strftime(date_format)

        origin = data.get("origin")
        destination = data.get("destination")
        if origin == destination:
            raise InvalidOriginDestinationException()
        return data

    @validates("origin")
    def validate_origin(self, origin):
        self._validate_port_or_region(origin)

    @validates("destination")
    def validate_destination(self, destination):
        self._validate_port_or_region(destination)

    def _validate_port_or_region(self, code_or_slug):
        region_exists = Region().exists(code_or_slug)
        port_exists = Port().exists(code_or_slug)

        if not region_exists and not port_exists:
            raise PortOrRegionNotFound(code_or_slug)


class RatesGetOutputSchema(Schema):
    """ /rates GET

    Parameters:
        - day (date)
        - average_price (date)
    """

    day = fields.String(required=True)
    average_price = fields.Integer(default=None, missing=None)
