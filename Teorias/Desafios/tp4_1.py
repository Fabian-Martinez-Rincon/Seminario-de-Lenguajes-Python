import csv
import os
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Teorias","Desafios", "netflix_titles.csv")


archivo = open(ruta_archivo, "r", encoding="utf-8")
csvreader = csv.reader(archivo, delimiter=',')

#encabezado = csvreader.__next__()
encabezado = next(csvreader)
print(encabezado)

print(csvreader)

for linea in csvreader:
    #if linea[1] == "TV Show" and linea[5] == "Argentina": 
    print(linea[2])

archivo.close()

