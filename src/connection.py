import contextlib
import sqlite3


@contextlib.contextmanager
def db():
    con = sqlite3.connect("practice.db")
    try:
        yield con
    finally:
        con.close()