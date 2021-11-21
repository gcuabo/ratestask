import pytest


@pytest.fixture
def rates_query_params():
    return {
        "date_from": "2016-01-01",
        "date_to": "2016-01-10",
        "origin": "CNGGZ",
        "destination": "EETLL",
    }
