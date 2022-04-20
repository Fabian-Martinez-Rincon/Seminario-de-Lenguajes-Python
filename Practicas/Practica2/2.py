
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
#Optimizar el count (most commont)
for dato in SinRepe:
    if texto.count(dato) > maximo:
        maximo = texto.count(dato)
        nom_Maximo = dato

print("El nombre que se repitio mas fue " , nom_Maximo, "con un todal de ", maximo)


#class Counter(builtins.dict)
# |  Counter(iterable=None, /, **kwds)
# |
# |  Dict subclass for counting hashable items.  Sometimes called a bag
# |  or multiset.  Elements are stored as dictionary keys and their counts
# |  are stored as dictionary values.
# |
# |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
# |
# |  >>> c.most_common(3)                # three most common elements
# |  [('a', 5), ('b', 4), ('c', 3)]
# |  >>> sorted(c)                       # list all unique elements
# |  ['a', 'b', 'c', 'd', 'e']
#-- Más  --