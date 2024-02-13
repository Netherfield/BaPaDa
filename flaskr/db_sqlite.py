import sqlite3
import csv
import os

# database MySQL -> localhost, root, ''
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''
}


# CONNESSIONE AL DB
def create_db_connection(db_name, db_dir):
    path_db = os.path.join(db_dir, db_name)
    if not os.path.exists(path_db):
        try:
            connection = sqlite3.connect(path_db)
            connection.row_factory = sqlite3.Row
            print("db created")
        except Exception as e:
            print(e)
            print("Unable to create db")
    else:
        try:
            ...
        except Exception as e:
            print(e)
    return connection

# CREAZIONE TABELLA
def create_table(connection, name):
    cursor = connection.cursor()
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title VARCHAR(255),
            Author VARCHAR(255),
            Year INTEGER,
            Link VARCHAR(255)
        )
        """
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabella creata")

# CARICARE DATI NEL CSV
def load_data_from_csv(connection, table_name, csv_file_path):
    cursor = connection.cursor()
    with open(csv_file_path, 'r', encoding='utf-16') as file:
        next(file)  # Skip the header row
        csv_data = csv.reader(file)
        for row in csv_data:
            cursor.execute(f"INSERT INTO {table_name} (Author, Title, Year, Link) VALUES (?,?,?,?);", row)
    connection.commit()
    print("Dati CSV importati con successo")

# ESECUZIONE QUERY
def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
        connection.commit()
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
