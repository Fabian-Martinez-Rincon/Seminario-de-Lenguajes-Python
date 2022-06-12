import os
import csv
os.getcwd()
print(os.getcwd())
titulos_2021 = os.path.join(os.getcwd(),"Teorias", "Clase_4_Archivos","titulos2021.csv")
from collections import Counter
archivo = open(titulos_2021, 'r', encoding="UTF-8")

csv_reader = csv.reader(archivo, delimiter=',')
paises = map(lambda fila: fila[3], csv_reader )
print(paises)
top_5 = Counter(paises).most_common()
print(f'Los 5 paises con más titulos: \n {dict(top_5)}')