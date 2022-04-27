#EJERCICIO 7: dado el archivo denominado [BBB_nuevo.csv]() que contiene los accesos al recurso BigBlueButton que usamos para las clases virtuales de la materia, se desea generar una función que retorne los 3 usuarios con menos actividad registrada.
#URL del cuaderno asignado 

import os
from collections import Counter
import csv
from typing import Iterable

def tres_menores (usuarios:Iterable[list[str]])-> list[tuple[str,int]]:
    listado_nombres = [user[1] for user in usuarios]
    tres_menos_frecuentes = Counter(listado_nombres).most_common()[:-4:-1]
    return tres_menos_frecuentes

usuarios_csv_path = os.path.join(os.getcwd(),'BBB_nuevo.csv')
with open(usuarios_csv_path, 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp, delimiter=',')
    print(tres_menores(reader)) 

