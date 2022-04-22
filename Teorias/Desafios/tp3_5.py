cadena = "hola como estan"
cadena = map(lambda x: chr(ord(x) + 1), cadena)
cadena = (''.join(map(str,cadena)))
print(cadena)



