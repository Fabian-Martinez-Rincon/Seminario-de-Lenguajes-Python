cadena = input("Ingresar una cadena: ")
cadena2 = input("Ingresar otra cadena: ")
cont1 = 0
cont2 = 0
for car in cadena:
    cont1+=1
for car in cadena2:
    cont2+=1
if (cadena>cadena2):
    print("La primera cadena es mas grande")
else:
    print("La segunda cadena es mas grande")