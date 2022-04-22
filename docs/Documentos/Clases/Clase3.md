<h1 align="center"> 🐍Clase 3 </h1>

### ```1) Primer Desafio``` [Resolución](#Desafio_1)

**Queremos escribir una función que imprima sus argumentos agregando de qué tipo son**

- Por ejemplo, podríamos invocarla de la siguiente manera:

```py
imprimo(1) --> 1 es de tipo <class 'int'>
imprimo(2, "hola") --> 2 es de tipo <class 'int'>, hola es de tipo <class 'str'>
imprimo([1,2], "hola", 3.2) --> [1, 2] es de tipo <class 'list', hola es de tipo <class 'str'>
```

¿Qué tiene de distinta esta función respecto a las que vimos antes o conocemos de otros lenguajes?

### ```2) Segundo Desafio``` [Resolución](#Desafio_2)

**Probar en casa este ejemplo y analizar el orden en el que definimos los parámetros.**

```python
 def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle):
    print("Mensaje original")
    print(mensaje_inicial)
    print("\nEn otros idiomas")
    print("-" * 40)
    for val in en_otro_idioma:
        print(val)
    print("\nEn detalle")
    print("-" * 40)
    for clave in en_detalle:
        print(f"{clave}: {en_detalle[clave]}")
    print("\nFuente: traductor de Google. ")
imprimo_muchos_valores("Hola",
    "hello", "Hallo", "Aloha ", "Witam", "Kia ora",
    ingles= "hello",
    aleman="Hallo",
    hawaiano="Aloha",
    polaco="Witam",
    maori="Kia ora")
```

### ```3) Tercer Desafio``` [Resolución](#Desafio_3)

- Queremos implementar una función que dada una cadena de texto, retorne las palabras que contiene en orden alfabético.

### ```4) Cuarto Desafio``` [Resolución](#Desafio_4)

- Queremos implementar una función que dada una colección con datos de usuarios de un determinado juego (por ejemplo nombre, nivel y puntaje), queremos retornar esta colección ordenada de acuerdo al nombre.

### ```5) Quinto Desafio``` [Resolución](#Desafio_5)

**sando expresiones lambda escribir una función que permita codificar una frase según el siguiente algoritmo:**

```
encripto("a") --> "b"
encripto("ABC") --> "BCD"
encripto("Rock2021") --> "Spdl3132"
```

Ejercicio_1
-----------

```python
from typing import Any
def imprimo(*args:Any): #El tipo any es cualquier tipo
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")  

imprimo(1)
print("-"*30)
imprimo(2, "hola")
print("-"*30)
imprimo([1,2], "hola", 3.2)
```

Ejercicio_2
-----------

```
Mensaje original
Hola

En otros idiomas
----------------------------------------
hello
Hallo
Aloha 
Witam
Kia ora

En detalle
----------------------------------------
ingles: hello
aleman: Hallo
hawaiano: Aloha
polaco: Witam
maori: Kia ora

Fuente: traductor de Google.
```

Ejercicio_3
-----------

```python
def ordeno1(cadena:str="ss"):
    lista = cadena.split()
    lista.sort(key=str.lower)
    #lista.sort()
    return lista

print(ordeno1("Hoy puede ser un gran día. "))
```

Ejercicio_4
-----------

```python
tipo_Usuarios = list[tuple[str,str,int]]
def ordeno3(usuarios:tipo_Usuarios):
    return sorted(usuarios, key=lambda usuario: usuario[1])
usuarios = [
    ('JonY BoY', 'Nivel3', 15),
    ('1962', 'Nivel1', 12),
    ('caike', 'Nivel2', 1020),
    ('Straka^', 'Nivel2', 1020),
]
print(type(usuarios))
print(ordeno3(usuarios))
```

Ejercicio_5
-----------

```python
cadena = "hola como estan"
cadena = map(lambda x: chr(ord(x) + 1), cadena)
cadena = (''.join(map(str,cadena)))
print(cadena)
```