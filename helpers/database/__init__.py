import sqlite3
from flask import g

from helpers.application import app

DATABASE_NAME = "avicola.db"


def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = sqlite3.connect(DATABASE_NAME)
    return conn


@app.teardown_appcontext
def close_connection(exception):
    print("------------ Tou finalizando a requisição!!!")
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()
