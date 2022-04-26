<h1 align="center"> 🐍Clase 2 </h1>

### ```1) Primer Desafio``` [Resolución](#Desafio_1)

- Dado el conjunto de datos con series y películas de Netflix, queremos:

  - 1) Guardar en otro archivo las peliculas agregadas en el año 2021.

  - 2) Los cinco (5) países con más producciones en Netflix.

### ```2) Segundo Desafio``` [Resolución](#Desafio_2)

- Implementar un programa que muestre un menú a través del cual se puedan visualizar los resultados del desafío 1.

  - Pueden usar la [librería console-menu](https://github.com/aegirhall/console-menu) analizada en clase.
  - Pueden agregar más opciones con los ejemplos mostrados en la clase

Desafio_1
---------

```python
import csv
import os
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Teorias","Desafios", "netflix_titles.csv")
archivo = open(ruta_archivo, "r", encoding="utf-8")
csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)
file = open("nuevoArchivo.txt", "w")
for linea in csvreader:
    if linea[7] == "2021": 
        file.write(linea[2] + os.linesep)
file.close()
archivo.close()
```

Desafio_2
---------

```python
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
def Imprimir(linesFile:list[str]):
    for line in linesFile:
        print (line)
file = open('nuevoArchivo.txt')
linesFile = file.readlines()

menu = ConsoleMenu("Title", "Subtitle")

menu_item = MenuItem(Imprimir(linesFile))

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)


file.close()
# Finally, we call show to show the menu and allow the user to interact
menu.show()


```