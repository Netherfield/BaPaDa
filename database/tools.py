import contextlib
import os
import sqlite3

def check_db_exists(museo, opere):
    filename = os.path.join(museo, f"{opere}.db")
    if not os.path.exists(filename):
        return False
    try:
        conn = sqlite3.connect(filename)
        conn.close()
        return True
    except sqlite3.OperationalError as e:
        if "not found" in str(e):
            return False
        else:
            raise

def create_or_open_db(opere, db_folder="Museo"):
    filename = os.path.join(db_folder, opere)
    if not os.path.exists(filename):
        try:
            conn = sqlite3.connect(f"{filename}")
            print(f"Created new database {opere}.")
        except Exception as e:
            print(f"Unable to create database '{opere}' due to:", str(e))
            return False
    else:
        try:
            conn = sqlite3.connect(
                filename)  # controllare perché mi dice che è un Unexpected argument per il check_last_error
            print(f"Opened existing database {opere}.")
        except Exception as e:
            print(f"Unable to open database '{opere}', reason:", str(e))
            return False
    contextlib.closing(opere)
    return conn


def connection_exists(opere):
    conn = None
    try:
        conn = create_or_open_db(opere)
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


def create_db_conn(opere, db_folder="museo"):
    if connection_exists(opere):
        conn = opendb(opere)
    else:
        conn = createdb(opere, db_folder)

    return conn


def opendb(opere):
    try:
        conn = create_or_open_db(opere)
    except Exception as e:
        print(f"Can't connect to db '{e.__str__()}'. Check if file exist.")
        return None
    else:
        return conn


def createdb(opere, db_folder="museo"):
    conn = create_or_open_db(opere, db_folder)
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
