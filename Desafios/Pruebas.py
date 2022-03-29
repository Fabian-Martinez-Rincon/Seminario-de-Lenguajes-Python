meses = {"enero": 31, "febrero": 28, "marzo": 31}
meses1 = meses
meses2 = meses.copy()
print(id(meses))
print(id(meses1))
print(id(meses2))


vocales = [ "a", "e","i", "o", "u"]
print(vocales[1:3] )

def imprimo_contacto(nombre, celu):
#print(type(celu))
    print(nombre, celu)
contacto = {"nombre": "Messi", "celu": 12345}
imprimo_contacto(**contacto)
