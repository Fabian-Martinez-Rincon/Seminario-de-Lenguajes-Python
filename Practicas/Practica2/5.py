from sqlite3 import DatabaseError


Frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
Frase = Frase.lower()
palabra = palabra.lower()
Datos = Frase.count(palabra)
print('La cantidad de ocurrencias es:', Datos)