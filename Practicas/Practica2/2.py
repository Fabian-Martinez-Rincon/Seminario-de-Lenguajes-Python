
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

# lista con palabras sin repetir
SinRepe = set(texto.lower().split())

maximo = -1
nom_Maximo = ""

for dato in SinRepe:
    if texto.count(dato) > maximo:
        maximo = texto.count(dato)
        nom_Maximo = dato

print("El nombre que se repitio mas fue " , nom_Maximo, "con un todal de ", maximo)