from core.models.base import BaseModel
from core.models.price import Price


def test_price(rates_query_params):
    price = Price()
    assert isinstance(price, BaseModel)
    assert callable(price.get_rates)


def test_price_origin_is_region(rates_query_params):
    rates_query_params["origin"] = "scandinavia"
    records = Price.get_rates(**rates_query_params)
    assert isinstance(records, list)
    assert len(records) > 0


def test_price_destination_is_region(rates_query_params):
    rates_query_params["destination"] = "scandinavia"
    records = Price.get_rates(**rates_query_params)
    assert isinstance(records, list)
    assert len(records) > 0
