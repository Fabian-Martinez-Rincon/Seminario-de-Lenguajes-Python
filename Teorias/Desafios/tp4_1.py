#• Dado el conjunto de datos con series y películas de Netflix, queremos:
#1- guardar en otro archivo las peliculas agregadas en el año 2021.
#2- los cinco (5) países con más producciones en Netflix.

import csv
import os
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Teorias","Desafios", "netflix_titles.csv")
archivo = open(ruta_archivo, "r", encoding="utf-8")
csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)
file = open("nuevoArchivo.txt", "w")
for linea in csvreader:
    if linea[7] == "2021": 
        file.write(linea[2] + os.linesep)
file.close()
archivo.close()
