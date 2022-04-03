palabra = "casa"

repetida = False
contador = 0
while (repetida == False)& (contador <len(palabra)):
    if (palabra.count(palabra[contador])>1):
        repetida = True
    contador+=1
if repetida:
    print("La palabra no es un Heterograma")
else:
    print("La palabra es un Heterograma")
