import os
import sqlite3
from sqlite3 import *
from pathlib import Path

def check_db_exists(db_name) -> bool:
    try:
        conn = sqlite3.connect(f"{db_name}.db")
        conn.close()
        return True
    except FileNotFoundError:
        print("DB doesn't exist")
        return False

def create_or_open_db(museo):
    conn = None
    museo_path = Path(__file__).resolve().parent / f"{museo}.db"
    if check_db_exists:
        conn = connection_exists(museo_path)
    else:
        conn = create_database(museo)
def create_database(museo):
    try:
        conn = sqlite3.connect(museo)
        conn.close()
        print('db creato')
    except sqlite3.Error as e:
        if 'no such table' in str(e):
            return False
        raise
    else:
        return True

def connection_exists(museo) -> sqlite3.Connection:
    conn = None
    try:
        if os.path.isfile(f"{museo}.db"):
            conn = sqlite3.connect(f"{museo}.db", check_same_thread=False)
            cursor = conn.cursor()
    except FileNotFoundError as err:
        print(f"Errore: Database '{museo}' non trovato.")
        print(err)
    except Exception as err:
        print(f"Errore imprevisto durante l'apertura del database '{museo}'. Dettagli: {err}")
    finally:
        if conn is not None:
            conn.close()
    return conn

# def create_or_open_db(museo):
#     conn = None
#     museo_path = Path(__file__).resolve().parent / f"{museo}.db"
#     if connection_exists(museo):
#         conn = connect()
#     conn = sqlite3.connect(museo)


def create_tables():
    conn = connect(os.path.join(os.path.expanduser("~"), "Desktop", "museo.db"))
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

