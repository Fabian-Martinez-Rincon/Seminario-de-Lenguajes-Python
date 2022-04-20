palabra = "Escriba"#o frase 
#Hacer un split de las palabras
#identificar si es una palabra o una frase
#filter.count(caracteres)
print(len(palabra))
repetida = False
contador = 0
while (repetida == False)& (contador <len(palabra)):
    if (palabra.count(palabra[contador])>1):
        repetida = True
    contador+=1
#Uso filter
if repetida:
    print("La palabra no es un Heterograma")
else:
    print("La palabra es un Heterograma")

#if len(set(palabra)) != len (palabra):
#    print('no es heterograma)
#else:
#    print('es heterograma'