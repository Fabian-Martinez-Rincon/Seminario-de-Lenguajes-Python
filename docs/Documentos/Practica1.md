<h1 align="center"> 💻Practica 1 </h1>

## ``1 Python 2022- Practica``

### ``1.1 Objetivos``

- Preparar el entorno de trabajo que utilizarán a lo largo de la materia instalando las herramientas básicas.
- Aprender a escribir nuestro primer programa Python y ejercutarlo
- Crear nuestro primer repositorio local y subir el código a un repositorio remoto

### ``1.2 Objetivos``
Para el acceso al material tendremos un [sitio web alternativo](https://python-unlp.github.io/2022/) para que puedan consultar.

 #### ``1)`` Realizar la instalación de Python 3.X recomendado 3.10

Para esta instalación de Python 3.X recomendado 3.10

Para esta actividad existen 3 alternativos: *Instalar python en forma local, para windows seguir esta [guía](https://python-unlp.github.io/2022/guias/06_instalar_python/). * Utilizar una herramienta para realizar la instalación en tu sistema operativo: [Conda](https://docs.conda.io/en/latest/) o [Pyenv](https://pypi.org/project/pyenv/). Para conocer un poco más qué son entornos virtuales puede consultar esta [Guía](https://python-unlp.github.io/2022/guias/07_entornos_virtuales/) Utilizar directamente la Máquina Virtual provista por la cátedra. Para esto es necesario que se instale en el sistema operativo una herramiento de virtualización como [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

 #### ``2)`` Escriba en un archivo llamado adivino.py el siguiente programa en Python (similar al que vieron en la teoría [Clase 1 de la teoría](https://catedras.linti.unlp.edu.ar/pluginfile.php/103493/mod_resource/content/0/Clase_1_Introducci%C3%B3n.pdf))

 ```python
 ## Adivina adivinador....
import random
numero_aleatorio = random.randrange(5)
gane = False
print("Tenés 3 intentos para adivinar un entre 0 y 99")
intento = 1
while intento < 4 and not gane:
    numeroIngresado = int(input('Ingresa tu número: '))
    if numeroIngresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
 ```

 Luego, modifiquelo para que:
 - Genero un número aleatorio entre 0 y 100
 - Los nombres de las variables respeten la guía de estilo del lenguaje
 - Se de 5 posibilidades para adivinar el número.

## ``1.3 Git``

 ### ``1.3.1 Instroducción``
 Como ya vimos Git es una herramienta muy buena que nos permite manejar versiones de nuestro código de manera distribuida con nuestro equipo de trabajo.

 Para poder realizar esto es necesario contar con un Servidor de Git aparte de tener la herramienta instalada en su [máquina](https://python-unlp.github.io/2022/guias/04_instalar_git/)

 ## ``2 Primer entrega 😬``

 - ***Puntos:*** 10.
 - ***Fecha limite de entrega:*** Viernes, 25 de marzo de 2022, 23:59.
 - ***Modalidad de entrega:***
 
 1) Crea tu propio repositorio en [Github](https://github.com/) siguiendo esta [Guía](https://python-unlp.github.io/2022/guias/04_instalar_git/)
 2) Agregar el archivo ***adivino.py*** con las modificaciones solicitadas.
 3) Agrega el ***README.md*** con tu nombre y número de alumnx.
 4) Sube todos los cambios a tu repositorio en Github
 5) Agregar el link del repositorio a la [tarea](https://catedras.linti.unlp.edu.ar/mod/assign/view.php?id=34349) en el curso.