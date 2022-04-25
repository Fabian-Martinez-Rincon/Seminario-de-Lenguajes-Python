import csv
import os

def Paises(csv_reader:list[list[str]]):
    orden = []
    for linea in csv_reader:
        #print(linea[5])
        orden.append(linea[5])
    orden = (set(orden))
    orden = sorted(orden)
    print(orden)



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
