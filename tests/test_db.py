def test_db_connection(app):
    db_conn = app.db()
    assert not db_conn.closed


def test_fetch_many(app):
    from core.db import fetch_many

    test_query = "SELECT * from ports"
    results = fetch_many(test_query)
    assert isinstance(results, list)
    assert isinstance(results[0], tuple)


def test_fetch_one(app):
    from core.db import fetch_one

    test_query = "SELECT * from ports"
    results = fetch_one(test_query)
    assert isinstance(results, tuple)
