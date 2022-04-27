<h1 align="center"> 💻Practica 2 </h1>

## ``Seminario de Lenguaje Python 2022``

### ```2.1 Parte 1```

- ```1)``` Tomando el texto del **README.md** de [numpy](https://github.com/numpy/numpy), imprima todas las líneas que contienen ``http`` o ``https``.  [Resolución](#Ejercicio_1)

Recordar: * ``split():`` ¿qué caracter utilizarían para separar? * string **in** frase: para saber si un substring está incluido dentro de una frase * ¿podemos preguntar si un string se encuentra en una frase antes de recorrer la lista de palabras?

- ``2)`` Indique la palabra que aparece mayor cantidad de veces en el texto del **README.md** de numpy. Recordemos algunas funciones de string: [Resolución](#Ejercicio_2)

```py
texto = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""
## lista con todas las palabras
print(texto.lower().split())
# lista con palabras sin repetir
print(set(texto.lower().split()))
```

```
['the', 'constants', 'defined', 'in', 'this', 'module', 'are:the', 'constants',
'defined', 'in', 'this', 'module', 'are:', 'string.ascii_letters', 'the',
'concatenation', 'of', 'the', 'ascii_lowercase', 'and', 'ascii_uppercase', 'constants', 'described', 'below.', 'this', 'value', 'is', 'not', 'localedependent.', 'string.ascii_lowercase', 'the', 'lowercase', 'letters',
"'abcdefghijklmnopqrstuvwxyz'.", 'this', 'value', 'is', 'not', 'localedependent', 'and', 'will', 'not', 'change.', 'string.ascii_uppercase', 'the',
'uppercase', 'letters', "'abcdefghijklmnopqrstuvwxyz'.", 'this', 'value', 'is',
'not', 'locale-dependent', 'and', 'will', 'not', 'change.']
{'string.ascii_uppercase', 'value', 'concatenation', 'ascii_lowercase', 'is',
'are:', 'ascii_uppercase', 'constants', 'locale-dependent.', 'and',
'string.ascii_letters', 'uppercase', 'this', 'of', 'string.ascii_lowercase',
'below.', 'locale-dependent', 'change.', 'defined', 'lowercase', 'the',
'module', 'not', 'are:the', "'abcdefghijklmnopqrstuvwxyz'.", 'will', 'in',
'described', 'letters'}
```

Investigue el módulo [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) para simplificar la resolución

### **2.1.1 Identificando mayúsculas, minúsculas y caracteres no letras**

```py
caracter = "T"
print(texto.split()[0].startswith(caracter))
```

¿Pero qué pasa si queremos saber indistintamente si la palabra comienza con dicha letra en minúscula o mayúscula?

```py
caracter = "t"
print(texto.lower().split()[0].startswith(caracter))
```

¿Y si el caracter ingresado no es una letra?

```py
import string
caracter = "?"
print(f"El caracter es una letra {caracter in string.ascii_letters}")
```

- ``3)`` Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string [Resolución](#Ejercicio_3)

- ``4)`` Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que deben cumplir y recomendaciones de escritura: [Resolución](#Ejercicio_4)

- **Título: 10 palabras como máximo**
- cada oración del resumen:

    - hasta 12 palabras: fácil de leer
    - entre 13-17 palabras: aceptable para leer
    - entre 18-25 palabras: difícil de leer
    - mas de 25 palabras: muy difícil

    Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:

```Py
evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit withresumen: Distributed agent-based modeling (ABM) on high-performance computing resources provide"""
```

En este ejemplo debería informar:

- titulo está ok
- Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy dificil de leer: 2

**Notas**: * investigue [Pattern Matching](https://peps.python.org/pep-0636/) para una solución simplificada. * ¿cuántas variables utilizó para guardar la cantidad de cada categoría, se podría usar alguna estructura?

- ``5`` Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas. [Resolución](#Ejercicio_5)

### **Ejemplo 1**

- **Para la frase:** ``Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.``
- **Palabra:** ``tres``
- **Resultado:** 3

### **Ejemplo 2**

- Para la frase: ``Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.``
- Palabra: ``tigres``
- Resultado: 2

### **Ejemplo 3**

- **Para la frase**: ``Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.``
- **Palabra**: ``TRISTES``
- **Resultado**: 3

### ```2.2 Parte 2```

- ``5)`` Retomamos el código visto en la teoría, que informaba si los caracteres ``@`` o ``!`` formaban parte de una palabra ingresada [Resolución](#Ejercicio_5_2)

```Py
cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣ ,→contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
    if car == "@" or car == "!":
        cant = cant + 1
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")
```

¿Cómo podemos simplificarlo?

- ``6)`` Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula. [Resolución](#Ejercicio_6)

```py
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
```

- ```7)``` Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la misma es un [Heterograma](https://es.abcdef.wiki/wiki/Isogram) (tenga en cuenta que el contenido del enlace es una traducción del inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres. [Resolución](#Ejercicio_7)

**Tener en cuenta** - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean letras. - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos la letra ``T`` y la letra ``t`` la misma NO será un Hererograma. - Para simplificar el ejercicio vamos a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:

```
>>> 'u' == 'ú'
```

| Entrada | ¿Heterograma? |
| ------------- | ------------- |
| cruzamiento  | Si  |
|  centrifugados | Si  |
|  portón | Si  |
|  casa | No  |
| día de sol  | No  |
|  con diez uñas | Si  |
| no-se-duplica  | Si  |


- ``8)`` Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la siguiente tabla de valores del juego Scrabble: [Resolución](#Ejercicio_8)


| Letra | Valor |
| ------------- | ------------- |
| A, E, I, O, U, L, N, R, S, T  | 1  |
| D, G  | 2  |
| B, C, M, P  | 3  |
| F, H, V, W, Y | 4  |
| K   | 5  |
| J, X  | 8  |
| Q, Z | 10  |


*Tenga en cuenta qué estructura elige para guardar estos valores en Python

### **Ejemplo 1**

- **Palabra:** ``solo``
- **valor:** 4

### **Ejemplo 2**

- **Palabra**: ``tomate``
- **valor**: 8

``9)`` La idea es tratar de programar una de las partes principales del juego ``Buscaminas``. La idea es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como la siguiente: [Resolución](#Ejercicio_9)

```py
[
'-*-*-',
'--*--',
'----*',
'*----',
]
```

Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo anterior, sería:

```py
[
'1*3*1',
'12*32',
'1212*',
'*1011',
]
```

**Nota:** Defina al menos una función en el código (si hay mas mejor) y documente las mismas con **docstring** que es lo que hacen.

- ``10)`` Trabajando con los contenidos de los archivos que pueden acceder en el curso: [Resolución](#Ejercicio_10)

- [nombres](https://catedras.linti.unlp.edu.ar/pluginfile.php/103770/mod_resource/content/1/nombres_1.txt)
- [eval1](https://catedras.linti.unlp.edu.ar/pluginfile.php/103771/mod_resource/content/1/eval1.txt)
- [eval2](https://catedras.linti.unlp.edu.ar/pluginfile.php/103772/mod_resource/content/1/eval2.txt)

Manipule estos archivos para realizar lo siguiente:
- Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
- Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
promedio.

- ``11)`` Con la información de los archivos de texto que se encuentran disponibles en el curso: [Resolución](#Ejercicio_11)

- [nombres_1](https://catedras.linti.unlp.edu.ar/pluginfile.php/103770/mod_resource/content/1/nombres_1.txt)
- [nombres_2](https://catedras.linti.unlp.edu.ar/pluginfile.php/103773/mod_resource/content/1/nombres_2.txt)

- Indique los nombres que se encuentran en ambos. **Nota:** pruebe utilizando list comprehension.

- Genere tres variables con la lista de notas y nombres que se incluyen en los archivos: nombres_1, eval1.txt y eval2.txt e imprima con formato los nombres de los estudiantes con las correspondientes nota y la suma de ambas como se ve en la [imagen](https://catedras.linti.unlp.edu.ar/mod/resource/view.php?id=34489)

### ```3 Segunda entrega```

- **Puntos:** 20.
- **Fecha límite de entrega:** Miércole 13 de Abril 23:59hs.
- **Modalidad de entrega:**

  - ``1`` Elige uno entre los ejercicios 10 y 11 que resolviste en esta práctica.
  - ``2)`` Publica el código de la resolución en un cuaderno de Jupyter Notebook en tu repositorio
creado en Github Github. Explicar en celdas con formato Markdown el significado de
los passos principales realizados para la resolución.
  - ``3)`` Agregar el link del repositorio a la tarea en el curso.


Ejercicio_1
-----------

```python
import os
clear = lambda: os.system('cls')
clear()
archivo = open("readme.txt","r")
links = []
for linea in archivo:
    if ("https" in linea)  :
        links.append(linea)
print(links)
archivo.close()
```

Ejercicio_2
-----------

```python
texto = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""
from collections import Counter

list_of_words=texto.lower().split()
c = Counter(list_of_words)
c.most_common(1)
print ("",c.most_common(1))
```

Ejercicio_3
-----------

```python
texto = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""
letra = input("Ingrese una letra: ")

SinRepe = (set(texto.lower().split()))
#mas cortes
for dato in SinRepe:
    if (dato[0].startswith(letra)):
        print(dato)
```

Ejercicio_4
-----------

```python
from cgitb import text
from posixpath import split
from time import process_time_ns

texto = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
syste"""

list_valores  = [0,0,0,0]
titulo = (((texto.split("\n")[0])).split()) #Saco el titulo
titulo.remove(titulo[0]) #Elimino el primer elemento que no cuenta para el titulo
#Usar el remplace('')
if (len(titulo)<=10):
    print("Titulo esta ok")

oraciones = texto.split(".")
oraciones.remove(oraciones[0]) #Elimino el titulo

for oracion in oraciones:
    if (len((oracion).split()) <= 12):
        list_valores [0]+=1
    elif((len((oracion).split()) >= 13) & (len((oracion).split()) <=17) ): 
        list_valores [1]+=1
    elif((len((oracion).split())>= 18) & (len((oracion).split()) <=25) ): 
        list_valores [2]+=1
    elif (len((oracion).split())>25):
        list_valores [3]+=1

print("Cantidad de oraciones fáciles de leer:", list_valores[0]," aceptables para leer:", list_valores[1], "dificil de leer: ",list_valores[2]," muy dificil de leer:" ,list_valores[3])

#Pattern Matching
```

Ejercicio_5
-----------

```python
Frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
Frase = Frase.lower()
palabra = palabra.lower()
Datos = Frase.count(palabra)
print('La cantidad de ocurrencias es:', Datos)
```

Ejercicio_5_2
-------------

```python
import re
cadena = "aaaaaaaaaa@!"
cumple = (len(cadena)>=10) & bool(re.search(r'@', cadena)) & bool(re.search(r'!', cadena))
if cumple:
    print("Contra Correcta")
#falta esto :( print("Ingresaste alguno de estos símbolos: @ o !" )
#count
```

Ejercicio_6
-----------

```python
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

lista = set((frase.lower()).split())
for palabra in lista:
    print(palabra)
```

Ejercicio_7
-----------

```python
palabra = "Escriba"#o frase 
#Hacer un split de las palabras
#identificar si es una palabra o una frase
#filter.count(caracteres)
print(len(palabra))
repetida = False
contador = 0
while (repetida == False)& (contador <len(palabra)):
    if (palabra.count(palabra[contador])>1):
        repetida = True
    contador+=1
#Uso filter
if repetida:
    print("La palabra no es un Heterograma")
else:
    print("La palabra es un Heterograma")

#if len(set(palabra)) != len (palabra):
#    print('no es heterograma)
#else:
#    print('es heterograma'
```

Ejercicio_8
-----------

```python
tabla = {"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":5,"jx":8,"qz":10}

palabra = "tomate"
total = 0
for letra in palabra:
    if letra in tabla:
        total+=tabla[letra]* letra.count(letra)
print(total)
#Accedo directo
#tratar de usar filter
#yield 
```

Ejercicio_9
-----------

```python
celdas = [
'-*-*-',
'--*--',
'----*',
'*----'
]
celdas = [list(col) for col in celdas]
def GuardarNumero(fila, columna):
    cant = 0

    Empieza_Fila = 0 if fila == 0 else -1
    Termina_Fila = 1 if fila == 3 else 2

    Empieza_Columna = 0 if columna == 0 else -1
    Termina_Columna = 1 if columna == 4 else 2

    for i in range(Empieza_Fila, Termina_Fila):
        for j in range(Empieza_Columna, Termina_Columna):
            if celdas[fila + i][columna + j] == "*":
                cant += 1
    return cant



x = 0
y = 0
print(celdas)
celdas_bombas = []
print("_"*30)
print("Las siguientes celdas tienen bombas")
for celda in celdas:
    x = 0
    for bomba in celda:
        if (bomba=="-"):
            celdas[y][x] = GuardarNumero(y,x)
            celdas_bombas.append([y,x])
            #print("La celda [", y,"],[",x,"] ")
        x+=1
    y+=1
#Pattern Matching 
print("_"*30)
print(celdas_bombas)

print(celdas)
```

Ejercicio_10
------------

```python
import string


f = open ('eval1.txt','r')
notas = ((f.read()).split("\n"))
f.close()
for index, nota in enumerate(notas):
    notas[index] = ((nota.replace(",","")))
#zip
#readline
notas.pop(-1) #Elimine el ultimo elemento ya que no me dejaba convertirlos porque era un string
int_list = list(map(int, notas))

f = open ('eval2.txt','r')
notas2 = ((f.read()).split("\n"))
f.close()
for index, nota in enumerate(notas2):
    notas2[index] = nota.replace(",","")

notas2.pop(-1)
int_list2 = list(map(int, notas2))


nuevasNotas:list[int] = []
for i in range(len(int_list)):
	nuevasNotas.append(int_list[i]+int_list2[i])

print(nuevasNotas)
# [111, 155, 100, 108, 99, 134, 78, 121, 33, 53, 74, 13, 48, 101, 106, 128, 97, 106, 76, 90, 21, 173, 62, 79, 100, 68, 142, 112, 87, 146, 148, 55, 140, 109, 103, 110, 137, 114, 65, 22, 105, 99, 24, 139, 126, 120, 84]

#_____________________________________________________


f = open ('nombres_3.txt','r')
nombres = ((f.read()).split("\n"))
f.close()
for index, nombre in enumerate(nombres):
    nombres[index] = ((nombre.replace(",","")))

print(nombres)

dict_from_list = dict(zip(nombres,nuevasNotas ))
print(dict_from_list)

promedio = sum(nuevasNotas) / len(nuevasNotas)
print(promedio)



for clave, valor in dict_from_list.items():
    if valor> promedio:
        print(clave)
```


Ejercicio_11
------------

```python
f = open ('eval1.txt','r')
notas = ((f.read()).split("\nro1"))
f.close()
for index, nota in enumerate(notas):
    notas[index] = ((nota.replace(",","")))

notas.pop(-1) #Elimine el ultimo elemento ya que no me dejaba convertirlos porque era un string
int_list = list(map(int, notas))

f = open ('eval2.txt','r')
notas2 = ((f.read()).split("\nro1"))
f.close()
for index, nota in enumerate(notas2):
    notas2[index] = nota.replace(",","")

notas2.pop(-1)
int_list2 = list(map(int, notas2))


nuevasNotas = []
for i in range(len(int_list)):
	nuevasNotas.append(int_list[i]+int_list2[i])

print(nuevasNotas)
# [111, 155, 100, 108, 99, 134, 78, 121, 33, 53, 74, 13, 48, 101, 106, 128, 97, 106, 76, 90, 21, 173, 62, 79, 100, 68, 142, 112, 87, 146, 148, 55, 140, 109, 103, 110, 137, 114, 65, 22, 105, 99, 24, 139, 126, 120, 84]

#_____________________________________________________


f = open ('nombres_3.txt','r')
nombres = ((f.read()).split("\nro1"))
f.close()
for index, nombre in enumerate(nombres):
    nombres[index] = ((nombre.replace(",","")))

print(nombres)

f = open ('nombres_2.txt','r')
nombres2 = ((f.read()).split("\nro1"))
f.close()
for index, nombre in enumerate(nombres2):
    nombres2[index] = ((nombre.replace(",","")))

print(nombres2)

nombresRepetidos = [nro1 for nro1 in nombres for nro2 in nombres2 if nro1 == nro2]
print("Nombres repetidos:", nombresRepetidos)

print("   {:<15} {:<10} {:<10} {:<10}".format("NOMBRE", "EVAL1", "EVAL2", "TOTAL"))
for i, estudiante in enumerate(zip(nombres, notas, notas2)):
    nombre, nota1, nota2 = estudiante
    nota1, nota2 = int(nota1), int(nota2)

    print(
        "{:<} {:<18} {:<10} {:<10} {:<10}".format(
            i, nombre, nota1, nota2, nota1 + nota2
        )
    )
```