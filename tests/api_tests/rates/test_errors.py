import pytest


@pytest.mark.parametrize(
    "date_from,date_to,origin,destination,expected_status_code",
    [
        ("", "2016-01-01", "CNGGZ", "EETLL", 400),
        ("2016-01-01", "", "CNGGZ", "EETLL", 400),
        ("2016-01-01", "2016-01-01", "", "EETLL", 400),
        ("2016-01-01", "2016-01-01", "EETLL", "", 400),
        ("", "", "", "", 400),
    ],
)
def test_incomplete_params(
    client, date_from, date_to, origin, destination, expected_status_code
):
    params = {
        "date_from": date_from,
        "date_to": date_to,
        "origin": origin,
        "destination": destination,
    }
    request = client.get(
        "/rates",
        query_string=params,
        headers={"User-Agent": "test-agent"},
        content_type="application/json",
    )
    assert request.status_code == expected_status_code
