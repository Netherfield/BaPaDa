import sqlite3
import csv

# database MySQL -> localhost, root, ''
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''
}

# SOSTITUIRE CON NOME DEL DATABASE
db_name = "database/sqldb/museo"

# CONNESSIONE AL DB
def create_db_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

# CREAZIONE TABELLA
def create_table(name):
    connection = create_db_connection()
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
def load_data_from_csv(table_name, csv_file_path):
    connection = create_db_connection()
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
