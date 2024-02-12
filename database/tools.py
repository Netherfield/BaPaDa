import os
import sqlite3
from sqlite3 import *


def _create_database(museo):
    try:
        conn = sqlite3.connect(museo)
        conn.close()
        print('db creato')
    except sqlite3.OperationalError as e:
        if 'no such table' in str(e):
            return False
        raise
    else:
        return True

def connection_exists(museo):
    database = os.path.join(os.path.dirname(__file__), museo)
    return _create_database(database)

def create_or_open_db(museo):
    if connection_exists(museo):
        return
    conn = sqlite3.connect(museo)


def create_tables():
    conn = connect(os.path.join(os.path.expanduser("~"), "Desktop", "opere.db"))
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Opere(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_n TEXT,
            title TEXT,
            year INTEGER,
            link TEXT
        );
    """)

    conn.commit()
    conn.close()

def load_data(opere):
    conn = connect(os.path.join(os.path.expanduser("~"), "Desktop", "opere.db"))
    cursor = conn.cursor()

    for opera in opere:
        cursor.execute("INSERT INTO opere VALUES (NULL, %s, %s, %s, %s)",
                       (opera["author_n"],
                        opere["title"],
                        opere["anno"],
                        opere["link"]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    opere = []
    load_data(opere)
