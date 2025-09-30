import sqlite3

def get_connection():
    conn = sqlite3.connect(":memory:")  # DB en memoria para pruebas
    conn.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)")
    return conn
