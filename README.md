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
<br>

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


 <details><summary> Clase_2_Secuencias_Funciones </summary><br>

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


<details><summary> Clase_3_Argumentos_lambda </summary><br>

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


<details><summary> Clase_4_Archivos </summary><br>
</details>


<details><summary> Clase_5_Repaso_archivos </summary><br>
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


















