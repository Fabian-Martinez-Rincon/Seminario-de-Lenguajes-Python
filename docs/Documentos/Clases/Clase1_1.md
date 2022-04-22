<h1 align="center"> 🐍Clase 1.1 </h1>

### ```1) Primer Desafio```  [Resolución](#Desafio_1)

- Escribir un programa que ingrese 4 palabras desde teclado e imprima aquellas que contienen la letra ```r```.
- **Pensar:** ¿Podemos usar la instrucción **for** tal cual la vimos la clase pasada para las 4 iteraciones?
- La sentencia **for** permite iterar sobre una **secuencia.**

Desafio_7
=========

```python
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