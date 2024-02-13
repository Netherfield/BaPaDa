from flask_manager import *
import time

def manager(sql=False):
    if sql:
        print("GG WP")
    else:
        print("WELCOME TO BADAPA Script")

        # path = input("inserisci path del .csv: ")
        path = "database/data/museum.csv"

        # nome_db = input("inserisci Nome DB: ")
        # TODO: correct variables in flask files to be generic
        nome_db = "museo"

        # table_name = input("inserisci Nome Tabella: ")
        # TODO: correct variables in flask files to be generic
        table_name = "quadri"

        db.create_server_connection()
        db.create_database(nome_db)
        db.create_db_connection()
        db.create_table(table_name)
        db.load_data_from_csv(table_name, path)
        print("CREAZIONE DB IN CORSO...")
        time.sleep(1)
        print("INTERROGANDO AI SU COME FARE...")
        time.sleep(1)
        print("ATTESA RISPOSTA...")
        time.sleep(1)
        print("BRB, HO DA FARE, ASPETTA!!!")
        time.sleep(1)
        print("IT'S GONNA WAYYY, YES???")
        time.sleep(2)

manager("ma")