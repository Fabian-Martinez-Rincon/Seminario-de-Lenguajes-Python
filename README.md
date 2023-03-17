<div align="center">

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Nomadiix/Seminario-de-Lenguajes-Python)
[![GitHub stars](https://img.shields.io/github/stars/Nomadiix/Seminario-de-Lenguajes-Python)](https://github.com/FabianMartinez1234567/Seminario-de-Lenguajes-Python/stargazers/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/Nomadiix/Seminario-de-Lenguajes-Python)](https://github.com/Nomadiix/Seminario-de-Lenguajes-Python)
 </div>

<h1 align="center"><img src="https://media.giphy.com/media/iQrDORShLPiqQ/giphy.gif" height="38" /> Seminario de Lenguajes Python </a>
 <img style="transform:scaleX(-1);" src="https://media.giphy.com/media/NLu0gwvgUMdxPtAHqS/giphy.gif" height="38" /></h1>


<div align="center">
  <img src="https://media.giphy.com/media/UTYINTtzZCs2DN4gsY/giphy.gif"/>
 </div>

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

- [🛡️ Defensa](/Defensa.md)
- 📚 Teoria (Desafios y Tareas)
    - [Clase 1](/docs/Documentos/Clases/Clase1.md)
    - [Clase 1.1](/docs/Documentos/Clases/Clase1_1.md)
    - [Clase 2](/docs/Documentos/Clases/Clase2.md)
    - [Clase 3](/docs/Documentos/Clases/Clase3.md)
    - [Clase 3.1](/docs/Documentos/Clases/Clase3_1.md)
    - [Clase 4](/docs/Documentos/Clases/Clase4.md)
    - [Clase 6](/docs/Documentos/Clases/Clase6.md)
    - [Clase 7](/docs/Documentos/Clases/Clase7.md)
- 🔧 Practica (Ejercicios)
    - [Ahorcado](/docs/Documentos/Ahorcado.md)
    - [Practica 1](/docs/Documentos/Practica1.md)
    - [Practica 2](/docs/Documentos/Practica2.md)
    - [Practica 3](/docs/Documentos/Practica3.md)

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">


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


<details><summary> Clase_5_Repaso_archivos </summary>

---

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


<details ><summary> Clase_6_Excepciones </summary>

---

## PySimpleGUI

- **read()**: devuelve una **tupla** con un **evento** y **los valores** de todos los elementos de entrada en la ventana.

```Python
import PySimpleGUI as sg      

sg.Popup('Mi  primera ventanita', button_color=('black', 'red'))
sg.PopupYesNo('Mi  primera ventanita', button_color=('black', 'green'))
sg.PopupOKCancel('Mi  primera ventanita', button_color=('black', 'grey'))
texto = sg.PopupGetText('Titulo', 'Ingresá algo')      
sg.Popup('Resultados', 'Ingresaste el siguiente texto: ', texto)

#Creamos una Ventana
sg.Window(title="Hola Mundo!", layout=[[]], margins=(100, 50)).read()
```

### Leemos los eventos por teclado

```Python
import PySimpleGUI as sg

layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
           [sg.Text('Ingresá segundo valor'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window("Segunda Demo", layout, margins=(200, 150))

while True:
    event, values = window.read()

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    print('Datos ingresados: ', values)

window.close()
```

### Layout: ¿cómo organizamos la UI?


Representa al esquema  o  diseño de nuestra UI: **cómo se distribuyen los elementos en la UI**.

```Python
layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
           [sg.Text('Ingresá segundo valor'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')] ]
```
### Elementos de la UI

- Acá van algunos disponibles en PySimpleGUI

	- Buttons: File Browse, Folder Browse, Color chooser, Date picker, etc.
	- Checkbox, Radio Button, Listbox    
	- Slider, Progress Bar 
	- Multi-line Text Input, Scroll-able Output  
	- Image, Menu, Frame, Column, Graph, Table

## Excepciones

### NameError

```Python
XX = 10
try:
    print(XX1)
except NameError:
    print("Usaste una variable que no está definida")
```

### KeyError

```Python
bandas = {
    "William Campbell": {"ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
    "Buendia": {"ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
    "Lúmine": {"ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"},
    "La Renga": {"ciudad": "XXXX", "ref": "ALGUNA"},
    "Divididos": {"ciudad": "XXXX", "ref": "xxx"}}
mis_bandas: = []
nombre_banda =  input("Ingresá el nombre de la banda que te gusta")

try:
     mis_bandas.append({"banda": nombre_banda, "url":bandas[nombre_banda]})
except KeyError:
    print("Ingresaste el nombre de una banda que no tengo registrada")
                            
print(mis_bandas)
```

### finally

Siempre se ejecuta al final del bloque Try. (Cosa que cuando tenemos una except no pasaria)

### else

Se ejecuta unicamente si no hubo except, podemos imprimir un mensaje indicando que no hubo inconvenientes

</details>


<details><summary> Clase_7_Intro_POO </summary>

---

### Objeto Jugador

- El método **\_\_init__() se invoca automáticamente** al crear el objeto.

```Python
class Jugador():
    """ Define la entidad que representa a un jugador en el juego"""
    def __init__(self, nom="Tony Stark", nic="Ironman"):
        self.nombre = nom
        self.nick = nic
        self.puntos = 0
    #Métodos
    def incrementar_puntos(self, puntos):
        self.puntos += puntos

tony = Jugador()
bruce = Jugador("Bruce Wayne", "Batman")
print(tony.nombre)
print(bruce.nombre)
```

### Objetos SuperHeroe

<table >

<tr>
<td> SuperHeroe</td> <td> imprimo_villanos</td>
</tr>

<tr>
<td>
 
```Python
class SuperHeroe():
    """ Esta clase  define a un superheroe 
    villanos:  representa a los enemigos 
    de todos los superhéroes
    """  
    villanos = []
        
    def __init__(self, nombre, alias):
        self.nombre = nombre
        self.enemigos = []
                
    def get_nombre(self):
        return self.nombre
  
    def get_enemigos(self):
        return self.enemigos
        
    def agregar_enemigo(self, otro_enemigo):
        "Agrega un enemigo a los enemigos del superhéroe"
        
        self.enemigos.append(otro_enemigo)
        SuperHeroe.villanos.append(otro_enemigo)
```


</td>
<td>

```Python
# OJO que esta función  está FUERA de la clase
def imprimo_villanos(nombre, lista_de_villanos):
    "imprime  la lista de todos los villanos de nombre"
    print("\n"+"*"*40)
    print(f"Los enemigos de {nombre}")
    print("*"*40)
    for malo in lista_de_villanos:
        print(malo)
        
batman = SuperHeroe( "Bruce Wayne", "Batman")
ironman = SuperHeroe( "Tony Stark", "ironman")

batman.agregar_enemigo("Joker")
batman.agregar_enemigo("Pinguino")
batman.agregar_enemigo("Gatubela")

ironman.agregar_enemigo("Whiplash")
ironman.agregar_enemigo("Thanos")
```


 
</td>
</tr>
 
</table>



```Python
imprimo_villanos(batman.get_nombre(), batman.get_enemigos())
imprimo_villanos(ironman.get_nombre(), ironman.get_enemigos())

imprimo_villanos("todos los superhéroes", SuperHeroe.villanos)
```

### Python nos permite hacer lo siguiente (No es buena Practica)

```Py
class SuperHeroe:
    pass

tony = SuperHeroe()  
tony.nombre = "Tony Stark"
tony.alias = "Ironman"
tony.soy_Ironman = lambda : True if tony.alias == "Ironman" else False

tony.soy_Ironman()
tony.nombre

del tony.nombre
tony.nombre
```

### No es publico

```Python
class Jugador():
    "Define la entidad que representa a un jugador en el juego"
    def __init__(self, nom="Tony Stark", nic="Ironman"):
        self._nombre = nom
        self.nick = nic
        self.puntos = 0
    #Métodos
    def incrementar_puntos(self, puntos):
        self.puntos += puntos

tony = Jugador()
print(tony._nombre)
```

### No es taaan publico

```Python
class CodigoSecreto:
    '''¿¿¿Textos con clave??? '''

    def __init__(self, texto_plano, clave_secreta):
        self.__texto_plano = texto_plano
        self.__clave_secreta = clave_secreta

    def desencriptar(self, clave_secreta):
        '''Solo se muestra el texto si la clave es correcta'''
        
        if clave_secreta == self.__clave_secreta:
            return self.__texto_plano
        else:
            return ''
```

# Entonces... respecto a lo público y privado

## Respetaremos las convenciones

### Todo identificador que comienza con **"_"** será considerado privado.

# Algunos métodos especiales

Mencionamos antes que los "__" son especales en Python. Por ejemplo, podemos definir métodos con estos nombres:

- \_\_lt__, \_\_gt__, \_\_le__, \_\_ge__ 
- \_\_eq__, \_\_ne__

En estos casos, estos métodos nos permiten comparar dos objetos con los símbolos correspondientes:

- x<y invoca  x.\_\_lt\_\_(y),
- x<=y invoca x.\_\_le\_\_(y), 
- x==y invoca x.\_\_eq\_\_(y), 
- x!=y invoca x.\_\_ne\_\_(y),
- x>y invoca x.\_\_gt\_\_(y), 
- x>=y invoca x.\_\_ge\_\_(y).

```Python
class Jugador:
    """ .. """
    def __init__(self, nom="Tony Stark", nic="Ironman"):
        self._nombre = nom
        self.nick = nic
        self.puntos = 0
    def __lt__(self, otro):
        return (self._nombre < otro._nombre)
    def __eq__(self, otro):
        return (self.nick == otro.nick)
    def __ne__(self, otro):
        return (self._nombre != otro._nombre)

tony = Jugador()
bruce = Jugador("Bruce Wayne", "Batman")

if bruce < tony:
    print("Mmmm.... Algo anda mal..")
print("Son iguales" if tony == bruce else "Son distintos")

# Mmmm.... Algo anda mal..
# Son distintos

```

### El método \_\_str__

```Python
class Jugador:
    """ .. """
    def __init__(self, nom="Tony Stark", nic="Ironman"):
        self._nombre = nom
        self.nick = nic
        self.puntos = 0
    def __str__(self):
        return (f"{self._nombre}, mejor conocido como {self.nick}")
    def __lt__(self, otro):
        return (self._nombre < otro._nombre)
    def __eq__(self, otro):
        return (self.nick == otro.nick)
    def __ne__(self, otro):
        return (self._nombre != otro._nombre)
tony = Jugador()
bruce = Jugador("Bruce Wayne", "Batman")

print(tony)
print(tony if tony == bruce else bruce)
```

---

## Herencia

```Python
class Jugador:
    def __init__(self, nombre, juego="Tetris", tiene_equipo=False, equipo=None):
            self.nombre = nombre
            self.juego = juego
            self.tiene_equipo = tiene_equipo
            self.equipo = equipo
    def jugar(self):
            if self.tiene_equipo:
                    print (f"{self.nombre} juega en el equipo {self.equipo} al {self.juego}")
            else:
                    print(f"{self.nombre} juega solo al {self.juego}")

class JugadorDeFIFA(Jugador):
    def __init__(self, nombre, equipo):
            Jugador.__init__(self, nombre, "FIFA", True, equipo)

class JugadorDeLOL(Jugador):
    def __init__(self, nombre, equipo):
            Jugador.__init__(self, nombre, "LOL")
            
nico = JugadorDeFIFA('Nico Villalba', "Guild Esports")
nico.jugar()
faker = JugadorDeLOL("Faker", "SK Telecom")
faker.jugar()

# Nico Villalba juega en el equipo Guild Esports al FIFA
# Faker juega solo al LOL
```

### Herencia Múltiple

```Python
class Jugador:
    def __init__(self, nombre, juego="No definido", tiene_equipo= False, equipo=None):
        self.nombre = nombre
        self.juego = juego
        self.tiene_equipo = tiene_equipo
        self.equipo = equipo
        
    def jugar(self):
        if self.tiene_equipo:
            print (f"{self.nombre} juega en el equipo {self.equipo} al {self.juego}")
        else:
            print(f"{self.nombre} juega solo al {self.juego}")

class Deportista:
    def __init__(self, nombre, equipo = None):
        self.nombre = nombre
        self.equipo = equipo
   
    def jugar(self): 
        print (f"Mi equipo es {self.equipo}")
class JugadorDeFIFA(Jugador, Deportista):
    def __init__(self, nombre, equipo):
        Jugador.__init__(self, nombre, "PS4", True, equipo)
        Deportista.__init__(self,nombre, equipo)

class JugadorDeLOL(Deportista, Jugador):
    def __init__(self, nombre, equipo):
        Jugador.__init__(self, nombre, "LOL")
        Deportista.__init__(self, nombre, equipo)
nico = JugadorDeFIFA('Nico Villalba', "Guild Esports")
nico.jugar()
faker = JugadorDeLOL("Faker", "SK Telecom")
faker.jugar()
```

- Ambas clases bases tienen definido un método **jugar**.
    - En este caso, se toma el método de la clase más a la **izquierda** de la lista.

- Por lo tanto, es MUY importante el orden en que se especifican las clases bases. 


# Resumiendo...

## Objetos  y clases

- La  **clase** define las propiedades y los métodos de los objetos.

- Los **objetos** son instancias de una clase.

- Cuando se crea un objeto, se ejecuta el método **\_\_init()__** que permite inicializar el objeto.

- La definición de la clase especifica qué partes son privadas y cuáles públicas.


# Mensajes y métodos

TODO el procesamiento en este modelo es activado por mensajes entre objetos.

- El **mensaje** es el modo de comunicación entre los objetos. Cuando se invoca una función de un objeto, lo que se está haciendo es **enviando un mensaje** a dicho objeto.
- El **método** es la función que está asociada a un objeto determinado y cuya ejecución sólo puede desencadenarse a través del envío de un mensaje recibido.


</details>


<details><summary> Clase_8_Iteradores_y_excepciones </summary>

---

## Super y Herencia Múltiple

```Python
class A():
    def __init__(self):
        print("Soy A")

class B():
    def __init__(self):
        print("Soy B")

class C(B, A):
    def __init__(self):
        print("Soy C")
        super().__init__()
obj = C()

# Soy C
# Soy B
C.__mro__
# (__main__.C, __main__.B, __main__.A, object)
```

### Decoradores

```Python
def decorador(funcion):
    def funcion_interna():
        print("Antes de  invocar a la función.")
        funcion()
        print("Después de invocar a la función.")
    return funcion_interna

@decorador
def decimos_hola():
    print("Hola!")

decimos_hola()

# Antes de  invocar a la función.
# Hola!
# Después de invocar a la función.
```

### Excepciones Personalizadas

```Python
try:
    raise ExcepcionRara("Hola mundo")
    
except ExcepcionRara as e:
    print(f"Ups! Se produjo la excepción rara!! {e}")
```

### Algunas convenciones

```Python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

try:
    raise InputError("xxx","hola")
except InputError as e: 
    print(e)
#('xxx', 'hola')
```

</details>


<details><summary> Clase_9_Intro_DS </summary>

---

### Pandas

```Python
import os
import pandas as pd

archivo_netflix = os.path.join(os.getcwd(),  "netflix_titles.csv")
data_set = pd.read_csv(archivo_netflix, encoding='utf-8')
print(data_set)
```

### Algunas operaciones
- len(data_set) `Cuantas filas?`
- data_set.shape `Cuantas filas y columnas?`
- data_set.columns `Cuales son las columnas`
- data_set["type"] `Filtrar por la columna type`
- data_set["type"].unique() `Que no aparezcan valores repetidos`
- columna = data_set["type"] `Cuantos contenidos hay de cada tipo`

### DataFrame

```Python
datos = {
        'tenista': ['Novak Djokovic', 'Rafael Nadal', 'Roger Federer', 'Ivan Lendl', 'Pete Sampras', 'John McEnroe', 'Bjorn Borg'],
        'pais': ['Serbia', 'España', 'Suiza', 'República Checa','Estados Unidos', 'Estados Unidos', 'Suecia'],
        'gran_slam': [20, 21, 20, 8, 14, 7, 11],
        'master_1000': [37, 36, 28, 22, 11, 19, 15],
        'otros': [5, 1, 6, 5, 5, 3, 2]
         }
labels_filas = ["H01", "H02", "H03", "H04", "H05", "H06", "H07"]
df = pd.DataFrame(data=datos, index=labels_filas)
print(df)
tenistas = df["tenista"] 
# Accedemos a los datos de una columna
print(tenistas)
# Accedemos a una fila
fila = df.loc["H03"]  
print(fila)
# Vemos los datos de la primera fila
df.iloc[0] 
x = df.iloc[0]
x["tenista"]
# Un Conjunto
# Por Filas
df.loc["H03":"H06"]
# Por Columnas
df[["tenista","master_1000"]]
# Un dato especifico
el_mejor = df.at["H03","tenista"]
```

#### Que tenistas ganaron mas de 20g Gran Slam

```Python
df[df["gran_slam"] >= 20]
```

### Podemos guardar el dataframe en archivos

```Python
# En formato csv
tv_shows_ar.to_csv("ShowsAR.csv")
# En formato json
tv_shows_ar.to_json("ShowsAR.json")
```

</details>


<details><summary> Clase_10_Intro_Ds_Pandas </summary>

---



</details>


<details><summary> Clase_11_Intro_Testing </summary>

---

Assert

- Esta sentencia realiza una comprobación de una condición, y en caso de ser falsa, levanta la excepción `AssertionError` en forma general es `assert condicion`

```Python
assert sum([1, 2, 3]) == 6

# Equivalente a 
if sum([1, 2, 3]) != 6:
    raise AssertionError()
```

### Pruebas

```Python
def calcular_promedio(lista):
	cant_elementos = len(lista)
	return 0 if cant_elementos == 0 else sum(lista)/cant_elementos
assert calcular_promedio([1, 2, 3]) == 2.0, "Deberia dar 2.0"
assert calcular_promedio([1]) == 1.0, "Deberia dar 1.0"
assert calcular_promedio([]) == 0, "Deberia dar 0"

def sumar(a, b):
	assert type(a) == int, "El primer argumento debería ser un entero"
	assert type(b) == int, "El segundo argumento debería ser un entero"
	return a+b
sumar(1,2)
#sumar(15.2, 2)

# "El primer argumento debería ser un entero"

def test_case1():
	assert calcular_promedio([]) == 0, "Debería dar 0"
def test_case2():
	assert calcular_promedio([1]) == 1.0, "Debería dar 1.0"
def test_case3():
	assert calcular_promedio([1, 2, 3]) == 2.0, "Debería dar 2.0"
if __name__ == "__main__":
	test_case1()
	test_case2()
	test_case3()
	print("Tests pasados!") # Imprime esto
```

### Tipos de test

- Test de unidad
- Test de integración
- Test de sistema
- Test de aceptación

## ¿Cómo definimos nuestros tests?

- Debemos definir nuestros casos de prueba en clases que heredan de la clase unittest.TestCase.
- Los métodos asociados a los test deben comenzar con el prefijo “test”, de manera tal que puedan ser reconocidos por el test runner.
- En vez de utilizar la sentencia assert, cada test invoca a métodos definidos en unittest.TestCase tales como:
    - assertEqual(), assertNotEqual(): para chequear por un resultado esperado.
    - assertTrue(), assertFalse(): para verificar una condición.
    - assertRaises(): para verificar si se levantó una excepción.
    - La lista completa de métodos en la documentación oficial]

</details>


















