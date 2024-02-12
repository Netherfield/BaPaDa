import mysql.connector
import csv

# database MySQL -> localhost, root, ''
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''
}

# SOSTITUIRE CON NOME DEL DATABASE
db_name = "museo"

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
    print("DB creato")


# CONNESSIONE AL DB
def create_db_connection(name=None):
    if name:
        db_config["database"] = name
    else:
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

#CREAZIONE TABELLA
def create_table(name):
    create_table_query = f"""
        CREATE TABLE {name} (
            id INT(32) AUTO_INCREMENT,
            Quadro VARCHAR(255),
            Autore VARCHAR(255),
            Anno INT,
            Link VARCHAR(255),
            PRIMARY KEY(id)
        )
        """
    execute_query(create_table_query)
    print("tabella creata")

# CARICARE DATI NEL CSV
def load_data_from_csv(table_name, csv_file_path):
    connection = create_db_connection()
    cursor = connection.cursor()
    with open(csv_file_path, 'r') as file:
        next(file)  # Skip the header row
        csv_data = csv.reader(file)
        for row in csv_data:
            cursor.execute(f"INSERT INTO {table_name} (Quadro, Autore, Anno, Link) VALUES (%s,%s,%s,%s);", row)
    connection.commit()
    print("Dati CSV importati con successo")

# test code
# kill = "DROP DATABASE museo"
# if __name__ == '__main__':
    # conn = create_server_connection()
    # killer = conn.cursor()
    # killer.execute(kill)
#     create_server_connection()
#     create_database("museo")
#     create_db_connection()
#     create_table_query = """
#     CREATE TABLE quadri (
#         id INT(32) AUTO_INCREMENT,
#         Quadro VARCHAR(255),
#         Autore VARCHAR(255),
#         Anno INT,
#         PRIMARY KEY(id)
#     )
#     """
#     execute_query(create_table_query)
#     load_data_from_csv("quadri", "test-db/sample_csv.csv")