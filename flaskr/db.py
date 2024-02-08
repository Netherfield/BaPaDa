import mysql.connector
import csv

# database MySQL -> localhost, root, ''
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''
}

# SOSTITUIRE CON NOME DEL DATABASE
db_name = None

# CONNESSIONE AL SERVER
def create_server_connection():
    return mysql.connector.connect(**db_config)

# CREAZIONE DB
def create_database(name_db:str):
    connection = create_server_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {name_db}")
        print("Database creato con successo")
    except Exception as e:
        print(f"L'errore '{e}' è occorso")
    finally:
        cursor.close()
        connection.close()

# CONNESSIONE AL DB
def create_db_connection():
    db_config["database"] = db_name
    return mysql.connector.connect(**db_config)

# ESECUZIONE QUERY
def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
        connection.commit()
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# CARICARE DATI NEL CSV
def load_data_from_csv(table_name, csv_file_path):
    connection = create_db_connection()
    cursor = connection.cursor()
    with open(csv_file_path, 'r') as file:
        next(file)  # Skip the header row
        csv_data = csv.reader(file)
        for row in csv_data:
            cursor.execute(f"INSERT INTO {table_name} VALUES (%s,%s,%s);", row)
    connection.commit()
    print("Dati CSV importati con successo")

# test code
db_name = "museo"
create_db_connection()
create_table_query = """
CREATE TABLE quadri (
    Quadro VARCHAR(255),
    Autore VARCHAR(255),
    Anno INT
)
"""
# execute_query(create_table_query)
load_data_from_csv("quadri", "test-db/sample_csv.csv")