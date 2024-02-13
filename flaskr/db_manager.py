import flaskr.db_sqlite as db

NOME_DB = "museo"
TABLE_NAME = "quadri"
PATH = 'database/data/museum.csv'
DIR_DB = 'database/sqldb'

def manager(server=False):
    if server:
        print("we are not dealing with xampp, sql connection, etc")
        # db.create_server_connection()
    # connect to db and create tables
        try:
            db.create_database(NOME_DB)
            # db.create_db_connection()
        except Exception as e:
            print(e)
    else:
        try:
            connection = db.create_db_connection(NOME_DB, DIR_DB)
            print("missing?")
        except Exception as e:
        
            print(e)
    try:
        db.create_table(connection, TABLE_NAME)
    except Exception as e:
        print(e)
    try:
        db.load_data_from_csv(connection, TABLE_NAME, PATH)
    except Exception as e:
        print(e)

manager()



