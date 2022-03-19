<h1 align="center"> 💻Seminario de Lenguajes Python </h1>

- [Practica 1](/Documentos/Practica1.md)

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
