num = int( input("Ingresá un número: "))
if ((num % 2) == 0):
    print("El nro es multiplo de Dos")
elif((num % 3) == 0):
    print("El nro es multiplo de Tres")
elif((num % 5) == 0):
    print("El nro es multiplo de Cinco")
else:
    print("El nro no es multiplo de 2,3 o 5")