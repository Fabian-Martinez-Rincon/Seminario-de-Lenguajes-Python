<h1 align="center"> 🐍Clase 7 </h1>

### ```1) Primer Desafio```  [Resolución](#Desafio_1)

¿Dónde se puede producir una excepción? ¿Cuál o cuáles?

```python
mi_musica = {70: ["Stairway to heaven", "Bohemian Rhapsody"], 80: ["Dancing in the dark", "Welcome to the jungle", "Under pressure"], 2000:["Given up", "The pretender"]}
tema = input("Ingresá un nuevo tema (FIN para terminar): ")
while tema !="FIN":
    decada = int(input("ingresá a qué década pertenece: "))
    mi_musica[decada].append(tema)
    tema = input("Ingresá un nuevo tema (FIN para terminar): ")
```

### ```1) Primer Desafio```  [Resolución](#Desafio_2)

- Dado el dataset con datos de video juegos del Apple store.
- Armar un menú con PySimpleGUi que permita:
  - 1. listar los juegos gratuitos disponibles en idioma español.
  - 2. los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count).
- Los que deseen, lo pueden subir a GitHub y compartir solución con @clauBanchof
- Incluir manejo de excepciones donde consideren adecuado.
- Tambien pueden descargar el [archivo](https://archivos.linti.unlp.edu.ar/index.php/s/D0YR0jqOx1GQtSD)

***Ayuda:*** para recuperar las imágenes de los íconos podemos usar el módulo requests - Se instala
con pip: ***pip install requests**** - [+Info](https://realpython.com/python-requests/)

```python
# Ayuda para el punto 2
import requests
import os
juego = "Gloomhaven"
archivo = os.path.join(os.getcwd(), "archivos", juego)
icon_url = "https://cf.geekdo-images.com/original/img/lDN358RgcYvQfYYN6Oy2TXpifyM=/0x0/pic2437871.jpg"
icono = requests.get(icon_url)
with open(f'{archivo}.jpg', 'wb') as f:
    f.write(icono.content)
```

Desafio_1
---------

```python
mi_musica = {70: ["Stairway to heaven", "Bohemian Rhapsody"],80: ["Dancing in the dark", "Welcome to the jungle", "Under pressure"], 2000:["Given up", "The pretender"]} 
tema = input("Ingresá un nuevo tema (FIN para terminar): ")
while tema !="FIN":
    try:
        decada = int(input("ingresá a qué década pertenece: "))
        mi_musica[decada].append(tema)
    except ValueError:
        print("Para ingresar la decada, tenés que ingresar un número. Empecemos de nuevo...")
    except KeyError:
        print("""Por ahora, sólo tengo registradas las décadas: 70, 80 y 2000. Ingresá una de ellas. Empecemos de nuevo...""")
    tema = input("Ingresá un nuevo tema (FIN para terminar): ")
```

Desafio_2
---------

```python

```