def test_db_connection(app):
    db_conn = app.db()
    assert not db_conn.closed
