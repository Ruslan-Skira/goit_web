import logging

import psycopg2
from contextlib import contextmanager
from psycopg2 import OperationalError, DatabaseError


@contextmanager
def create_connection():  # Creating custom context manager
    """
    Create a database connection to a Postgres database.
    """
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='password')
        yield conn  # yield because you use @contextmanager and this is rule
        conn.close()  # that will be done after context mangager closed
    except OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")

