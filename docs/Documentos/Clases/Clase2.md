<h1 align="center"> 🐍Clase 2 </h1>

```1)``` [Resolución](#Desafio_1)

Vamos a modificar el código anterior para que imprima la cadena **R** si la palabra contiene la letra r y sino, imprimal ``NO TIENE R`` 

```2)``` [Resolución](#Desadfio_2)

**Ingresar palabras desde teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra** 

- ¿Qué estructura de control deberiamos utilizar para realizar esta interación?¿Podemos utilizar la sentencia for?

```3)``` [Resolución](#Desafio_3) 

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

```4)``` [Resolución](#Desafio_4)

**Necesitamos procesar las notas de los estudiantes de este curso Queremos saber:**

- Cúal es el promedio de las notas
- **Qué estudiantes** están por debajo del promedio

¿Qué diferencia hay con el desafio anterior?

- Deberíamos ingresar no sólo las notas, sino también los nombres de los estudiantes.
- ¿Qué soluciones proponen?

Desafio_1
---------
```Python
for i in range(4):
    cadena = input("Ingresá una palabra: ")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")
```

Desafio_2
---------
```Python
cadena = input("Ingresá una palabra: ")
while cadena != "FIN":
    if cadena[0] == (cadena[len(cadena)-1]):
        print("Empiezar y terminan con la misma letra")
        print(cadena)
    else:
        print("No empieza y termina con la misma letra")
    cadena = input("Ingresá una palabra: ")
```

Desafio_3
---------
```Python
notas = [ 4, 6, 7, 3, 8, 1, 10, 4]
total = 0

for i in range((len(notas))):
    print(notas[i])
    total += notas[i]
promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)
```

Desafio_4
---------
```Python
notas = {"Janis Joplin":10, "Elvis Presley": 9, "Bob Marley": 5, "Jimi Hendrix": 9}
notas["Bob Marley"]
total = 0


for key in notas:
    print (key, ":", notas[key])
    total += notas[key]

promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)
debajo_promedio = 0
for i in notas:
    if notas[i] < promedio:
        print("El estudiantes", i , "Esta por debajo del promedio")
        debajo_promedio+=+1
```