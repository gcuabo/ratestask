import pytest

from core.api.schema.rates import RatesGetInputSchema, RatesGetOutputSchema
from core.exceptions import (
    InvalidDateFromDateToException,
    InvalidOriginDestinationException,
    PortOrRegionNotFound,
)


def test_rate_input_no_errors(rates_query_params):
    schema = RatesGetInputSchema()
    errors = schema.validate(rates_query_params)
    assert errors == {}


@pytest.mark.parametrize(
    "field", [("date_from"), ("date_to"), ("origin"), ("destination")]
)
def test_rate_input_incomplete(rates_query_params, field):
    schema = RatesGetInputSchema()
    del rates_query_params[field]
    errors = schema.validate(rates_query_params)
    assert field in errors
    assert errors[field] == ["Missing data for required field."]


@pytest.mark.parametrize(
    "value,field,is_valid",
    [
        ("string_value", "date_from", False),
        ("2016-00-01", "date_from", False),
        ("2016-01-01", "date_from", True),
        ("string_value", "date_to", False),
        ("2016-30-30", "date_to", False),
        ("2016-12-01", "date_to", True),
    ],
)
def test_invalid_date(rates_query_params, value, field, is_valid):
    schema = RatesGetInputSchema()
    rates_query_params[field] = value
    errors = schema.validate(rates_query_params)
    if not is_valid:
        assert field in errors
        assert errors[field] == ["Not a valid date."]


def test_invalid_datefrom_dateto(rates_query_params):
    schema = RatesGetInputSchema()
    rates_query_params["date_from"] = "2020-01-02"
    rates_query_params["date_to"] = "2020-01-01"

    with pytest.raises(InvalidDateFromDateToException):
        schema.validate(rates_query_params)


def test_invalid_origin_destination(rates_query_params):
    schema = RatesGetInputSchema()
    rates_query_params["origin"] = rates_query_params["destination"]

    with pytest.raises(InvalidOriginDestinationException):
        schema.validate(rates_query_params)


@pytest.mark.parametrize(
    "value,field,is_valid",
    [
        ("does_not_exist", "origin", False),
        ("CNCWN", "origin", True),
        ("north_europe_sub", "origin", True),
        ("does_not_exist", "destination", False),
        ("CNCWN", "destination", True),
        ("north_europe_sub", "destination", True),
    ],
)
def test_port_or_region_does_not_exists(rates_query_params, field, value, is_valid):
    schema = RatesGetInputSchema()
    rates_query_params[field] = value
    if not is_valid:
        with pytest.raises(PortOrRegionNotFound):
            schema.validate(rates_query_params)
