from flask_manager import *
import time

def manager(option=None):
    if option:
        print("GG WP")
    else:
        print("WELCOME TO BADAPA Script")
        path = input("inserisci path del .csv: ")
        nome_db = input("inserisci Nome DB: ")
        table_name = input("inserisci Nome Tabella: ")
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
