from flask_manager import *

NOME_DB = "museo"
TABLE_NAME = "quadri"
DEF = '../database/test.csv'

def manager():
    print("WELCOME TO BADAPA Script")
    log = input("Hai già un DB? (Y/N): ")
    if log.lower() == "n":
        path = input("inserisci path del .csv: (DEF -> '../database/test.csv') ")
        if path.lower() == "def":
            path = DEF
            db.create_server_connection()
            try:
                db.create_database(NOME_DB)
            except Exception as exc:
                print(f"{exc}")
            db.create_db_connection()
            try:
                db.create_table(TABLE_NAME)
            except Exception as exc:
                print(f"{exc}")
            try:
                db.load_data_from_csv(TABLE_NAME, path)
                print("IT'S GONNA WAY?? YESS?!?")
            except Exception as exc:
                print(f"{exc}")
    else:
        print("Perchè mi hai runnato allora? BAH!")

manager()



