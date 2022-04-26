import csv
import os
import json

def Paises(csv_reader:list[list[str]]):
    for linea in csv_reader:
        if linea[1] == "TV Show" and linea[5] == "Argentina": 
            print(f"{linea[2]:<40} {linea[3]}")




ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Practica3", "netflix_titles.csv")


archivo = open(ruta_archivo, "r", encoding="utf-8")
csv_reader = csv.reader(archivo, delimiter=',')

#encabezado = csv_reader.__next__()
encabezado = next(csv_reader)
datos = list(csv_reader)
print(encabezado)
Paises(datos)





archivo.close()

import csv

archivo = open("bandas.txt")
archivo_csv = open("bandas.csv", "w")
bandas = json.load(archivo)
writer = csv.writer(archivo_csv)
writer.writerow(["Nombre", "Ciudad de procedencia", "Refencias"])
for banda in bandas:
10
