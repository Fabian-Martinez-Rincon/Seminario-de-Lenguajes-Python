<h1 align="center"> 🤖Desafios </h1>

## ```1) Primer Desafio```  [Resolución](#Desafio_1)

- Queremos ingresar un número desde teclado e imprimir si el número es o no par.
- ¿Cómo sería el pseudocódigo de esto?

```
Ingresar un número desde teclado
SI es par: 
    Mostrar mensaje: "es par"
SINO:
    Mostrar mensaje: "NO es par"
```

## ```2) Segundo Desafio``` [Resolución](#Desafio_2)

- Queremos ingresar un número desde el teclado e imprimir si es múltiplo de 2,3 o 5.
- **Pista:** Python tiene otra forma de la sentencia condicional: **if-elif-else**

## ```3) Tercer Desafio``` [Resolución](#Desafio_3)

- Dado una letra ingresada por el teclado, queremos saber si es mayúscula o minúscula.

## ```4) Cuarto Desafio``` [Resolución](#Desafio_4)

- Dado un caracter ingresado por el teclado, queremos saber si es una comilla o no.
- ¿Hay algún problema?

## ```5) Quinto Desafio``` [Resolución](#Desafio_5)

- Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.

## ```6) Sexto Desafio``` [Resolución](#Desafio_6)

- Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cuántas letras ``a`` contiene.

## ```7) Septimo Desafio``` [Resolución](#Desafio_7)

- Escribir un programa que ingrese 4 palabras desde teclado e imprima aquellas que contienen la letra ```r```.
- **Pensar:** ¿Podemos usar la instrucción **for** tal cual la vimos la clase pasada para las 4 iteraciones?
- La sentencia **for** permite iterar sobre una **secuencia.**

## ```8) Octavo Desafio``` [Resolución](#Desafio_8)

Vamos a modificar el código anterior para que imprima la cadena **R** si la palabra contiene la letra r y sino, imprimal ``NO TIENE R``

## ```9) Noveno Desafio``` [Resolución](#Desadfio_9)

**Ingresar palabras desde teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra**

- ¿Qué estructura de control deberiamos utilizar para realizar esta interación?¿Podemos utilizar la sentencia for?

## ```10) Decimo Desafio``` [Resolución](#Desafio_10)

**Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:**

- Cuál es el promedio de las notas
- Cuántos estudiantes están por debajo del promedio

¿Cómo estudiantes están por debajo del promedio?

```
Ingresar las notas
Calcular el promedio
Calcular cuántos tienen notas menores al promedio
```

Obviamente no. **Necesitamos tipos de datos que nos permiten guardar muchos valores**

Desafio_1
=========
```Py
num = int( input("Ingresá un número: "))
if num % 2 == 0:
    print("Es par")
else:
    print("No es par")
```
Desafio_2
=========
```Py
num = int( input("Ingresá un número: "))
if ((num % 2) == 0):
    print("El nro es multiplo de Dos")
elif((num % 3) == 0):
    print("El nro es multiplo de Tres")
elif((num % 5) == 0):
    print("El nro es multiplo de Cinco")
else:
    print("El nro no es multiplo de 2,3 o 5")
```
Desafio_3
=========

```Py
letra = input("Ingresar una letra: ")
if letra >="a" and letra <="z":
    print("Es minúscula")
elif letra >= "A" and letra <= "Z":
    print("Es mayúscula")
else:
    print("NO es una letra")
```
Desafio_4
=========

```Py
letra = input("Ingresar un caracter: ")
if letra == "\"":
    print("Es una comilla")
else:
    print("NO es una comilla")
```

Desafio_5
=========

```Py
cadena = input("Ingresar una cadena: ")
cadena2 = input("Ingresar otra cadena: ")
contador_1 = 0
contador_2 = 0
for car in cadena:
    contador_1+=1
for car in cadena2:
    contador_2+=1
if (cadena>cadena2):
    print("La primera cadena es mas grande")
else:
    print("La segunda cadena es mas grande")
```

Desafio_6
=========

```Py
cadena = input("Ingresar una cadena: ")
contador_a = 0
for car in cadena:
    if (car == "a"):
        contador_a+=1
print("La cantidad de letras a es: " , contador_a)
```

Desafio_7
=========
```Py
for i in range(4):
    cadena = input("Ingresá una palabra: ")
    if "r" in cadena:
        print(cadena)

#for elem in range(4):
#    cadena = input('Ingresa una cadena: ')
#    encontro = False
#    i=0
#    while(i < len(cadena)) and encontro == False:
#        if cadena[i] == "r":
#            print(cadena)
#            encontro = True
#        i=i+1
```
Desafio_8
=========
```Py
for i in range(4):
    cadena = input("Ingresá una palabra: ")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")
```

Desafio_9
=========
```Py
cadena = input("Ingresá una palabra: ")
while cadena != "FIN":
    if cadena[0] == (cadena[len(cadena)-1]):
        print("Empiezar y terminan con la misma letra")
        print(cadena)
    else:
        print("No empieza y termina con la misma letra")
    cadena = input("Ingresá una palabra: ")
```