import random
numero_aleatorio = random.randrange(100)
ganador_aleatorio = False
print("Tenés 3 intentos para adivinar un entre 0 y 99")
intento_aleatorio = 1
while intento_aleatorio <= 5 and not ganador_aleatorio:
    numeroIngresado = int(input('Ingresa tu número: '))
    if numeroIngresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento_aleatorio))
        ganador_aleatorio = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento_aleatorio += 1
if not ganador_aleatorio:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))