import contextlib
import os
import sqlite3
from pathlib import Path

def check_db_exists(museo, mostra):
    filename = os.path.join(museo, f"{mostra}.db")
    if not os.path.exists(filename):
        return False
    try:
        conn = sqlite3.connect(mostra)
        conn.close()
        return True
    except sqlite3.OperationalError as e:
        if "not found" in str(e):
            return False
        else:
            raise

def create_or_open_db(mostra, db_folder="Museo"):
    filename = os.path.join(db_folder, mostra)
    if not os.path.exists(filename):
        try:
            conn = sqlite3.connect(f"{filename}")
            print(f"Created new database {mostra}.")
        except Exception as e:
            print(f"Unable to create database '{mostra}' due to:", str(e))
            return False
    else:
        try:
            conn = sqlite3.connect(
                filename)  # controllare perché mi dice che è un Unexpected argument per il check_last_error
            print(f"Opened existing database {mostra}.")
        except Exception as e:
            print(f"Unable to open database '{mostra}', reason:", str(e))
            return False
    contextlib.closing(mostra)
    return conn


def connection_exists(mostra):
    conn = None
    try:
        conn = create_or_open_db(mostra)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table info(opere);").fetchone()
        conn.close()
        return True
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            return False
        else:
            raise
    finally:
        if conn is not None:
            conn.close()


def create_db_conn(mostra, db_folder="museo"):
    if connection_exists(mostra):
        conn = opendb(mostra)
    else:
        conn = createdb(mostra, db_folder)

    return conn


def opendb(mostra):
    try:
        conn = create_or_open_db(mostra)
    except Exception as e:
        print(f"Can't connect to db '{e.__str__()}'. Check if file exist.")
        return None
    else:
        return conn


def createdb(mostra, db_folder="museo"):
    conn = create_or_open_db(mostra, db_folder)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Opere(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_n TEXT,
            title TEXT,
            year INTEGER,
            link TEXT
        );
    """)
        conn.commit()
        conn.close()
    return conn


FIle_DB = Path(__file__).parent / "mostra"

if __name__ == "__main__":
    opere = "evento"
    # mi da problema Shadows name 'mostra' from outer scope

    if not check_db_exists(opere, FIle_DB):
        print(f"Creating new DB for {opere}")
        conn = create_db_conn(opere, str(FIle_DB))
        if conn is not None:
            print("Database created or open correctly.")

        else:
            print("Impossible to find a connection")

    else:
        print(f"The DB for {opere} already exist")

# Qui sotto metto gli errori comparsi fino ad ora
# nel caso vogliate controllare
# line 45 AttributeError: 'bool' object has no attribute 'cursor'
# at     cursor = conn.cursor()
#              ^^^^^^^^^^^
# line 103 same error at     conn = create_db_conn(opere, str(FIle_DB))
#                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# line 60, in create_db_conn
#     if connection_exists(mostra):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^
# line 56, in connection_exists
#     conn.close()
#     ^^^^^^^^^^