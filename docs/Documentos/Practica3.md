<h1 align="center"> 💻Practica 3 </h1>

### ```Objetivos```

- Manejo de archivos
- Módulo os
- Módulo datetime

## ```Archivos CSV```

- Datos de Netflix

Veamos el archivo [netflix_titles.csv](https://www.kaggle.com/shivamb/netflix-shows) con el que estuvieron trabajando en la teoría

```python
path_files = "files"
archivo_net = "netflix_titles.csv"
```

- ¿Cómo accederían al archivo?
- ¿En qué directorio guardarían estos datos?
- ¿Qué cosas hay que tener en cuenta?

```python
import csv
import os.path
import os
path_arch = os.path.join(os.getcwd(), path_files)
```

- Vemos los datos que tenemos, consultando los nombres de las columnas

```python
archivo = open(os.path.join(path_arch, archivo_net), "r")
data_net = csv.reader(archivo, delimiter=',')
header , datos = next(data_net), list(data_net )
header
```

- Recorremos el archivos para conocer las información que contiene

```python
for linea in datos:
    print(linea)
```

### ```1.1 Ejercicios```

## `1)` [Resolución](#ejercicio1)

Encontrar qué tipo de shows tiene un país determinado.

- Realizar una función que informe todos los países que existen.
- Realizar una función que dado un país informe si es parte de la línea del show pasado como
argumento. Nota: utilice las funciones vistas de lambda(utilizando la función definida), map
para informar los tipos de shows (valores únicos) en que participa un país.

Analizar: 

- ¿En qué número de columna está el país?
- Como en algunos casos hay varios países en un show debemos separarlos y quedarnos con
valores únicos.

## `2)` [Resolución](#ejercicio2)

Informe la lista de países del archivo en orden alfabéticamente creciente.

## `3)` [Resolución](#ejercicio3)

Informe los shows de un año determinado, realice una función que reciba un año y la línea como argumentos.

## `Fechas - datatime`

[Documentación datatime](https://docs.python.org/3/library/datetime.html)

```python
import datetime
```

El módulo datetime crea un objeto con el cual podemos realizar operaciones para cálculo de fechas.

```
x = datetime.datetime.now()
x
```

- Como saber qué número de día de la semana es hoy

```
x.hour
```

- Para guardar los datos en archivos se debe guardar en string indicando el formato en que queremos guardarla.

```python
horario_juego = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
horario_juego
```

### ```2.1 Ejercicios```

-  En base al [archivo](https://archivos.linti.unlp.edu.ar/index.php/s/q9b3rCrlhOS1yWU) analizar las fechas de los logs:

```python
import os
logs = 'BBB_nuevo.csv'
with open(os.path.join(path_arch, logs)) as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )
for linea in logs_recurso:
    print(linea[0])
```

Analicemos cómo calcular el día de la semana que corresponde el log, el dato está guardado como
string y para hacer consults debemos convertirlo a objeto datetime. El segundo argumento de la
función strptime corresponde al [formato](https://docs.python.org/3/library/datetime.html), donde debemos indicar cómo se encuentra cada dato:

- %d = dia
- %m = mes
- %Y = año, si fuera la forma corta(22) corresponde %y
- luego tiene un espacio
- %H = hora
- %M = minutos

```python
formato = "%d/%m/%Y %H:%M"
print(datetime.datetime.strptime(linea[0], formato).weekday())

dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado','domingo']
nro_dia = datetime.datetime.strptime(linea[0], formato).weekday()
dias_semana[nro_dia]
datetime.datetime.strptime(linea[0], formato).weekday()
```



## `4)` [Resolución](#ejercicio4)

Indique los días de la semana que más registros hubo:


## `5)` [Resolución](#ejercicio5)

Calcule cuántos dias pasaron entre el primer registro y el último

Ejercicio_1
-----------

```python
import csv
import os
import json

def Paises(csv_reader:list[list[str]]):
    for linea in csv_reader:
        if linea[1] == "TV Show" and linea[5] == "Argentina": 
            print(f"{linea[2]:<40} {linea[3]}")

ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Practica3", "BBB_nuevo.csv")

archivo = open(ruta_archivo, "r", encoding="utf-8")
csv_reader = csv.reader(archivo, delimiter=',')

#encabezado = csv_reader.__next__()
encabezado = next(csv_reader)
datos = list(csv_reader)
print(encabezado)
Paises(datos)
archivo.close()
```

Ejercicio_2
-----------

```python
import csv
import os

def Paises(csv_reader:list[list[str]]):
    orden = []
    for linea in csv_reader:
        orden.append(linea[5])
    orden = (set(orden))
    orden = sorted(orden)
    print(orden)
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Practica3", "netflix_titles.csv")
archivo = open(ruta_archivo, "r", encoding="utf-8")
csv_reader = csv.reader(archivo, delimiter=',')
encabezado = next(csv_reader)
datos = list(csv_reader)
Paises(datos)
archivo.close()
```

Ejercicio_3
-----------

```python
import csv
import os

def Paises(csv_reader:list[list[str]]):
    for linea in csv_reader:
        if linea[7] == "2021" : 
            print(linea[7])

ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Practica3", "netflix_titles.csv")
archivo = open(ruta_archivo, "r", encoding="utf-8")
csv_reader = csv.reader(archivo, delimiter=',')

encabezado = next(csv_reader)
datos = list(csv_reader)
print(encabezado)

Paises(datos)

archivo.close()
```

Ejercicio_4
-----------

```python
import csv
import os
from datetime import date
import datetime 
import calendar
from collections import Counter

def findDay(fecha:str): 
    born = datetime.datetime.strptime(fecha,"%d/%m/%Y %H:%M").weekday() 
    return (calendar.day_name[born]) 

#3/03/2022 07:22

ruta = os.path.dirname(os.path.realpath("."))

path_arch = os.path.join(ruta, "Practica3")
ruta = os.path.join(path_arch, 'BBB_nuevo.csv')

with open(ruta,"r", encoding="utf-8") as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )

dias_semanales:list[str]

dias_semanales = Counter([findDay(fecha[0]) for fecha in logs_recurso])
print(dias_semanales.most_common(7))
```

Ejercicio_5
-----------

```python
import csv
from operator import length_hint
import os
from datetime import date
import datetime 
import calendar
from collections import Counter

def findDay(fecha:str): 
    born = datetime.datetime.strptime(fecha,"%d/%m/%Y %H:%M").weekday() 
    return (calendar.day_name[born]) 

#3/03/2022 07:22

ruta = os.path.dirname(os.path.realpath("."))

path_arch = os.path.join(ruta, "Practica3")
ruta = os.path.join(path_arch, 'BBB_nuevo.csv')

with open(ruta,"r", encoding="utf-8") as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )

dias_semanales:list[str]

print(logs_recurso[0][0])
fechas = logs_recurso[0][0].split('/')
dia = int(fechas[0])
mes = int(fechas[1])
anio = int(fechas[2][0:4])



a = datetime.datetime(anio, mes, dia, 00, 00) 

fechas2 = logs_recurso[len(logs_recurso)-1][0].split('/')
dia2 = int(fechas2[0])
mes2 = int(fechas2[1])
anio2 = int(fechas2[2][0:4])

b = datetime.datetime(anio2, mes2, dia2, 00, 00) 
c = a-b  
print('Difference: ', c) 
```
