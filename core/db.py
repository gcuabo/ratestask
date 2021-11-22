import psycopg2


def db():
    from flask import current_app as app

    con = psycopg2.connect(
        "dbname='{}' user='{}' host='{}' password='{}'".format(
            app.config["DB_NAME"],
            app.config["DB_USER"],
            app.config["DB_HOST"],
            app.config["DB_PASSWORD"],
        )
    )

    return con


def fetch_many(raw_query: str) -> tuple:
    from flask import current_app as app

    try:
        conn = app.db()
        cursor = conn.cursor()
        cursor.execute(raw_query)
        records = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    return records


def fetch_one(raw_query: str) -> type:
    from flask import current_app as app

    try:
        conn = app.db()
        cursor = conn.cursor()
        cursor.execute(raw_query)
        record = cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    if record[0]:
        return record
    return None


def execute(raw_query: str) -> None:
    from flask import current_app as app

    try:
        conn = app.db()
        cursor = conn.cursor()
        cursor.execute(raw_query)
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)
    finally:
        if conn:
            conn.commit()
            cursor.close()
            conn.close()
