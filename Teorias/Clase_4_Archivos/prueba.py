import os
import csv
os.getcwd()
print(os.getcwd())
titulos_2021 = os.path.join(os.getcwd(),"Teorias", "Clase_4_Archivos","netflix_titles.csv")
from collections import Counter
archivo = open(titulos_2021, 'r', encoding="UTF-8")

csv_reader = csv.reader(archivo, delimiter=',')
paises = map(lambda fila: fila[5], csv_reader )
print(paises)
top_5 = Counter(paises).most_common(5)
print(f'Los 5 paises con más titulos: \n {dict(top_5)}')