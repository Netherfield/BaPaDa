import csv

quadri = [("Quadro" + str(i), "Autore" + str(i), 1900 + i) for i in range(1, 51)]

with open('test-db/sample_csv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Quadro", "Autore", "Anno"])  # Scrivere l'intestazione
    writer.writerows(quadri)  # Scrivere i dati

print("File 'quadri.csv' creato con successo.")
