import pytest

import db

user_data = ("John", "john@example.com")


@pytest.fixture
def db_conn():
    """The name should be the same as argument."""
    with db.create_connection() as conn:
        yield conn


def test_db_operation(db_conn):
    cursor = db_conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fullname STRING,
                email STRING
        );
""")
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", user_data)
    db_conn.commit()
    r = cursor.execute("SELECT fullname, email FROM users")
    assert r.fetchone() == user_data
