def test_ping(app):
    client = app.test_client()

    request = client.get("/ping")
    assert request.status_code == 200
