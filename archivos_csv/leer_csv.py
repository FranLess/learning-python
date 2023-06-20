# importando la libreria built-in de csv
import csv
# abriendo el archivo csv con with open():
archivo_uri = 'archivos_csv\\datos.csv'
with open(archivo_uri) as archivo:
    # el reader() de csv devuelve un iterable de cada linea de csv
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
