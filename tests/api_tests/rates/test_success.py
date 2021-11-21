import pytest


def test_success(client, rates_query_params):
    request = client.get("/rates", query_string=rates_query_params)
    assert request.status_code == 200
    assert request.json
