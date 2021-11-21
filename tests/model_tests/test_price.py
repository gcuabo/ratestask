from core.db import execute
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


def test_rates_data(rates_query_params):
    # Test get rates accuracy

    insert_data_query = (
        "INSERT INTO prices values "
        "('CNGGZ', 'EETLL', '2017-01-01', 1),"
        "('CNGGZ', 'EETLL', '2017-01-03', 10),"
        "('CNGGZ', 'EETLL', '2017-01-03', 20),"
        "('CNGGZ', 'EETLL', '2017-01-03', 30),"
        "('CNGGZ', 'EETLL', '2017-01-03', 20)"
    )
    execute(insert_data_query)
    rates_query_params["date_from"] = "2017-01-01"
    rates_query_params["date_to"] = "2017-01-03"

    records = Price.get_rates(**rates_query_params)
    # Test that length is equals to the number of days
    assert len(records) == 3

    # assert that 2017-01-01 has null results because rows < 3
    day1_record = records[0]
    assert str(day1_record[0]) == "2017-01-01"
    assert day1_record[1] is None

    # assert that 2017-01-03 has an average because rows = 3
    last_day_record = records[-1]
    assert str(last_day_record[0]) == "2017-01-03"
    assert last_day_record[1] == 20

    # add data to 2017-01-01 so that rows >=3 and check that average is not None
    insert_data_query = (
        "INSERT INTO prices values "
        "('CNGGZ', 'EETLL', '2017-01-01', 1),"
        "('CNGGZ', 'EETLL', '2017-01-01', 1),"
        "('CNGGZ', 'EETLL', '2017-01-01', 1)"
    )
    execute(insert_data_query)
    records = Price.get_rates(**rates_query_params)
    day1_record = records[0]
    assert str(day1_record[0]) == "2017-01-01"
    assert day1_record[1] == 1
