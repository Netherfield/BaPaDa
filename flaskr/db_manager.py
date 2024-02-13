from flask_manager import *

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
        except Exception as e:
            print(e)
    else:
        try:
            db.create_database_lite(NOME_DB, DIR_DB)
        except Exception as e:
            print(e)
    db.create_db_connection()
    try:
        db.create_table(TABLE_NAME)
    except Exception as e:
        print(e)
    try:
        db.load_data_from_csv(TABLE_NAME, PATH)
    except Exception as e:
        print(e)



manager()



