cadena = input("Ingresá una palabra: ")
while cadena != "FIN":
    if cadena[0] == (cadena[len(cadena)-1]):
        print("Empiezar y terminan con la misma letra")
        print(cadena)
    else:
        print("No empieza y termina con la misma letra")
    cadena = input("Ingresá una palabra: ")