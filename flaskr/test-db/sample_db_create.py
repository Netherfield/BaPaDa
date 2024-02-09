import csv
def do():
    quadri = [("Quadro" + str(i), "Autore" + str(i), 1900 + i, "www.badapa.com/link" + str(i)) for i in range(1, 51)]

    with open('sample_csv.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Quadro", "Autore", "Anno", "Link"])  # Scrivere l'intestazione
        writer.writerows(quadri)  # Scrivere i dati

    print("File 'quadri.csv' creato con successo.")
do()