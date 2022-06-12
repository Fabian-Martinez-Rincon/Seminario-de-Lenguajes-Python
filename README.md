<h1 align="center"><img src="https://media.giphy.com/media/iQrDORShLPiqQ/giphy.gif" height="38" /> Seminario de Lenguajes Python </a>
 <img style="transform:scaleX(-1);" src="https://media.giphy.com/media/NLu0gwvgUMdxPtAHqS/giphy.gif" height="38" /></h1>

<div align="center">
<img src="https://media.giphy.com/media/KbUEFowFNOLSAsHT7u/giphy.gif" align="right" height="178" >



<table >
<tr>
<td> Teoria (Desafios y Tareas)</td> <td> Practica (Ejercicios)</td>
</tr>
<tr>
<td>
 
- [Clase 1](/docs/Documentos/Clases/Clase1.md)
- [Clase 1.1](/docs/Documentos/Clases/Clase1_1.md)
- [Clase 2](/docs/Documentos/Clases/Clase2.md)
- [Clase 3](/docs/Documentos/Clases/Clase3.md)
- [Clase 3.1](/docs/Documentos/Clases/Clase3_1.md)
- [Clase 4](/docs/Documentos/Clases/Clase4.md)
- [Clase 6](/docs/Documentos/Clases/Clase6.md)
- [Clase 7](/docs/Documentos/Clases/Clase7.md)

</td>
<td>


- [Ahorcado](/docs/Documentos/Ahorcado.md)
- [Practica 1](/docs/Documentos/Practica1.md)
- [Practica 2](/docs/Documentos/Practica2.md)
- [Practica 3](/docs/Documentos/Practica3.md)

 
</td>
</tr>
 
</table>

</div>

---


### 📖 Resumenes de cada tema:

<br>

<details ><summary>Clase_1_Introduccion</summary> 

---

```Python
cadena = "dos"
match cadena:
    case "uno":
        print("UNO")
    case "dos" | "tres":
        print("DOS O TRES")
    case _:
        print("Ups.. ninguno de los anteriores")
```

```Python
intento = 3
nombre = "claudia"
print(f'Hola {nombre} !!! Ganaste! y necesitaste {intento} intentos!!!')
x = 4
print(f"{x:2d} {x*x:3d} {x*x*x:4d}")
```

</details>


<details><summary> Clase_2_Secuencias_Funciones </summary>

---

#### Cargar una Lista desde teclado

```Python
def Ingresar(lista_de_notas:list[int]):
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
    while nota != -1:
        lista_de_notas.append(nota)
        nota = int(input("Ingresá una nota (-1 para finalizar)"))
    return lista_de_notas

lista_de_notas:list[int] = []
lista_de_notas=Ingresar(lista_de_notas)
print(lista_de_notas)

```

``Las tuplas no se pueden modificar``

#### Cargar un Diccionario desde teclado

```Python
def ingreso_notas():
""" Esta función retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}"))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    return dicci
notas_de_estudiantes = ingreso_notas()
notas_de_estudiantes
```

#### Los parametros pueden tener valores por defecto

```Python
def mi_musica(dicci_musica, nombre, tipo_musica="nacional"):
    if nombre in dicci_musica:
        interpretes = dicci_musica[nombre]
        for elem in interpretes[tipo_musica]:
            print(elem)
    else:
    print(f"¡Hola {nombre}! No tenés registrada música en esta colección")
mi_musica(nombre="vivi", tipo_musica="internacional", dicci_musica=dicci_musica)
```

#### Dato

```Python
def agrego(a, L=[]):
    L.append(a)
    return L
print(agrego(1))
print(agrego(2))
print(agrego(3))
```

#### Conjunto

Un conjunto es una colección de datos heterogéna, desordenada, NO indexada y sin elementos duplicados

```Python
bandas = {"AC/DC", "Metallica", "Greta Van Fleet", "Soda Stéreo", "Los Piojos"}
for elem in bandas:
    print(elem)
```

Operaciones con conjuntos
- Pensemos en las operaciones matemáticas sobre conjuntos:
    - in: retonar si un elemento pertenece o no a un conjunto.
    - |: unión entre dos conjuntos.
    - &: intersección entre dos conjuntos.
    - -: diferencia de conjuntos.


</details>


<details><summary> Clase_3_Argumentos_lambda </summary>

---

### Numero variable de parametros (Tupla)

#### `args` es una tupla que representa a los parámetros pasados.

```Python
def imprimo(*args):
    """ Esta función imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")
imprimo([1,2], "hola", 3.2) 
```

### Numero variable de parametros (Diccionario)

#### `args` es una diccionario que representa a los parámetros pasados.

```Python
def imprimo_otros_valores(**kwargs):
    """ ..... """
    for clave, valor in kwargs.items():
        print(f"{clave} es {valor}")
imprimo_otros_valores(banda1= 'Nirvana', banda2="Foo Fighters", banda3="AC/DC")
```

#### `global` y `nonlocal` permiten acceder a varables no locales a una función.

```Python
x = 0
def uno():
    x = 10
    def uno_uno():
        nonlocal x
        #global x
        x = 100
        print(f"En uno_uno: {x}")
    uno_uno()
    print(f"En uno: {x}") 
uno()
print(f"En ppal: {x}") 
```

### Atributos en Funciones

```Python
def calculo_promedio(notas):
    """ Esta función calcula el promedio de las notas recibida por parámetro.
    notas: es un diccionario de forma nombre_estudiante: nota
    """
    suma = 0
    for estu in notas:
        suma += notas[estu]
    promedio = 0 if len(notas)==0 else suma/len(notas)    
    return promedio

print(calculo_promedio.__doc__) 
print(calculo_promedio.__defaults__)
print(calculo_promedio.__name__)
```

- **funcion.\_\_doc__**: es el **docstring**.
- **funcion.\_\_name__**: es una cadena con el nombre la función.
- **funcion.\_\_defaults__**: es una tupla con los valores por defecto de los parámetros opcionales.


### Retorna una lista con las palabras en orden alfabetico 

```Python
def ordeno2(cadena:str):
    """ Implementación usando sorted"""
    lista = cadena.split()
    return sorted(lista, key=str.lower)
print(ordeno2("Hoy puede ser un gran día. "))
```

### Funciones Lambda

<h3>

```Python
 lambda parametros : expresion 
```

</h3>


### Ejemplo

```Python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print(f(42), g(42))
print(make_incrementor(22)(33))

# 44 48
# 55
```

### Función `map`

```Python
def doble(x):
    return 2*x
lista  = [1, 2, 3, 4, 5, 6, 7]
dobles = list(map(doble, lista))
print(dobles)
# [2, 4, 6, 8, 10, 12, 14]
```

### Función `map`

```Python
lista  = [1, 2, 3, 4, 5, 6, 7]
dobles = map(lambda x: 2*x, lista)
pares = list(filter(lambda x: x%2 == 0, lista))

print(dobles) # <map object at 0x00000144B50EDAB0>
print(pares)  # [2, 4, 6]
```

### Modulo `sys`

- Entre otras cosas, define:
    - `exit([arg])`: sale del programa actual;
    - `path`: las rutas donde buscar los módulos a cargar;
    - `platform`: contiene información sobre la plataforma.

## Tarea

- Averiguar cuándo un módulo se denomina **__main__**,

Un módulo puede definir funciones, clases y variables. Entonces, cuando el intérprete ejecuta un módulo, el variable \_\_name__ se establecerá como \_\_main__ si el módulo que se está ejecutando es el programa principa

</details>


<details ><summary> Clase_4_Archivos </summary>

---

# El módulo \_\_main__

- Las instrucciones ejecutadas en el nivel de llamadas superior del intérprete, ya sea desde un script o interactivamente, se consideran parte del módulo llamado **\_\_main__**, por lo tanto tienen su propio espacio de nombres global.

```Python
#módulo funciones
def uno():
    print("uno")
    print(f"El nombre de este módulo es {__name__}")

if __name__ == "__main__":
    uno()
```

### Función `open`

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
- **encoding**: sólo para modo texto. Por defecto, la codificación establecida en las [configuraciones del sistema](https://docs.python.org/3.8/library/codecs.html#module-codecs) 
- **errors**: sólo en modo texto. Es una cadena que dice qué hacer ante un error en la codificación/decodificación. ("strict", "ignore", ..)
- **newline**: sólo modo texto. Puede ser: None, '', '\\n', '\\r', y '\\r\\n'.

```python

archi = open("pp.xxx", "r+", encoding="UTF-8")

import locale
locale.getpreferredencoding()


import os

ruta = os.path.dirname(os.path.realpath("."))
ruta_completa = os.path.join(ruta, "ejemplo","clase4", "archivo.txt")
```

### Almaceno datos en un archivo

```Python
f = open('archivo.txt', 'w')
print(f.write('Hola, xxxxxx'))
print(f.write('Mundo!'))

f.close()
```

### Leemos datos en un archivo

```Python
f = open('archivo.txt', 'r')
x = f.read(4)
print(f.read())
x
```

## Json

Cuando quiero guardar información que tiene una estructura

- Pensemos en estos ejemplos:

	- Los puntajes cada vez que juego a un juego. Información tipo: nombre jugador,  puntaje, fecha.
	- El banco de preguntas: tema, enunciado, respuesta correcta.
	- Los Python Plus de los estudiantes por turnos: turno, nombre, apellido, num_alumno, cantidad_puntos, etc.

- Es un formato de intercambio de datos muy popular. Por ejemplo:

```json
	{"equipo": "Astralis",
	 "e-sport": "CSGO",
	 "pais": "Dinamarca"}
    o 
    [{"equipo": "Astralis",
	  "e-sport": "CSGO",
	  "pais": "Dinamarca"},
      {"equipo": "9z",
	  "e-sport": "CSGO",
	  "pais": "Argentina"}]
```
- [+Info](https://www.json.org/json-en.html)

```Python
import json
```

- Permite serializar objetos.
    - serializamos con: `dumps()` y `dump()`.
    - desserializamos con: `loads()` y `load()`.

### Implementación

```Python
import json

archivo = open("bandas.txt", "r")
datos = json.load(archivo)
datos_a_mostrar = json.dumps(datos, indent=4)
archivo.close()
```

## CSV

- CSV (Comma Separated Values).
- Es un formato muy común para importar/exportar desde/hacia hojas de cálculo y bases de datos.

- **csv.reader**: crea un objeto "iterador" que nos permite recorrer las líneas del archivo.

### Leemos el contenido completo

```Python
import csv

ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Clase_4_Archivos","netflix_titles.csv")

archivo = open(ruta_archivo, "r",encoding="UTF-8")
csvreader = csv.reader(archivo, delimiter=',')

#encabezado = csvreader.__next__()
encabezado = next(csvreader)

for linea in csvreader:
    if linea[1] == "TV Show" and linea[5] == "Argentina": 
        print(f"{linea[2]:<40} {linea[3]}")

archivo.close()
```

### Otra forma de hacer lo de arriba

```Python
archivo = open(ruta_archivo, "r",encoding="UTF-8")
csvreader = csv.reader(archivo, delimiter=',')

shows_ar = filter(lambda x:  x[5] == "Argentina" and x[1] == "TV Show", csvreader)
for elem in shows_ar:
    print(f"{elem[2]:<40} {elem[3]}")
    
print(shows_ar)
archivo.close()
```

### Creamos un Csv desde un Txt

```Python
import csv
import json

archivo = open("bandas.txt")
archivo_csv = open("bandas.csv", "w")

bandas = json.load(archivo)

writer = csv.writer(archivo_csv)
writer.writerow(["Nombre", "Ciudad de procedencia", "Refencias"])
for banda in bandas:
    writer.writerow([banda["nombre"], banda["ciudad"], banda["ref"]])

archivo.close()
archivo_csv.close()
#type(writer)
```

### DoctReader

```Python
archivo_cvs = open("bandas.csv", "r")
csvreader = csv.DictReader(archivo_cvs, delimiter=',')

for linea in csvreader:
    print(linea["Nombre"])

archivo_csv.close()
```

</details>


<details><summary> Clase_5_Repaso_archivos </summary><br>

### import os

```python
import os
os.getcwd()
#'c:\\Users\\fabian\\Desktop\\Seminario-de-Lenguajes-Python\\Teorias\\Clase_4_Archivos'
ruta_completa = os.path.join(os.getcwd(), ruta_archivos)

archivo_netflix = os.path.join(ruta_completa, "netflix_titles.csv")
titulos_2021 = os.path.join(ruta_completa, "titulos2021.csv")
```

### with

```Python
# Abro el dataset
with open(archivo_netflix, encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    # Creo el archivo .csv de salida
    with open(titulos_2021, 'w', encoding='utf-8') as salida:
        writer = csv.writer(salida)

        # Agrego el encabezado
        writer.writerow(reader.__next__())

        # Escribo sólo los titulos estrenados en 2021
        writer.writerows(filter(lambda titulo: titulo[7] == '2021', reader))
```

### Ejemplo Raro

```Python
import os
import csv
from collections import Counter

titulos_2021 = os.path.join(os.getcwd(),"Teorias", "Clase_4_Archivos","netflix_titles.csv")
archivo = open(titulos_2021, 'r', encoding="UTF-8")

csv_reader = csv.reader(archivo, delimiter=',')
paises = map(lambda fila: fila[5], csv_reader )
print(paises)
top_5 = Counter(paises).most_common(5)
print(f'Los 5 paises con más titulos: \n {dict(top_5)}')
```

</details>


<details><summary> Clase_6_Excepciones </summary><br>


</details>


<details><summary> Clase_7_Intro_POO </summary><br>
</details>


<details><summary> Clase_8_Iteradores_y_excepciones </summary><br>
</details>


<details><summary> Clase_9_Intro_DS </summary><br>
</details>


<details><summary> Clase_10_Pandas_Copa_America </summary><br>
</details>


<details><summary> Clase_11_Intro_Testing </summary><br>
</details>


















