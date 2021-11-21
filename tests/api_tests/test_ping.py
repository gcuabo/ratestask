def test_ping(client):
    request = client.get("/ping")
    assert request.status_code == 200
