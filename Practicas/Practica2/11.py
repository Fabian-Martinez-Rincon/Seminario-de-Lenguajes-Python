f = open ('eval1.txt','r')
notas = ((f.read()).split("\nro1"))
f.close()
for index, nota in enumerate(notas):
    notas[index] = ((nota.replace(",","")))

notas.pop(-1) #Elimine el ultimo elemento ya que no me dejaba convertirlos porque era un string
int_list = list(map(int, notas))

f = open ('eval2.txt','r')
notas2 = ((f.read()).split("\nro1"))
f.close()
for index, nota in enumerate(notas2):
    notas2[index] = nota.replace(",","")

notas2.pop(-1)
int_list2 = list(map(int, notas2))


nuevasNotas = []
for i in range(len(int_list)):
	nuevasNotas.append(int_list[i]+int_list2[i])

print(nuevasNotas)
# [111, 155, 100, 108, 99, 134, 78, 121, 33, 53, 74, 13, 48, 101, 106, 128, 97, 106, 76, 90, 21, 173, 62, 79, 100, 68, 142, 112, 87, 146, 148, 55, 140, 109, 103, 110, 137, 114, 65, 22, 105, 99, 24, 139, 126, 120, 84]

#_____________________________________________________


f = open ('nombres_3.txt','r')
nombres = ((f.read()).split("\nro1"))
f.close()
for index, nombre in enumerate(nombres):
    nombres[index] = ((nombre.replace(",","")))

print(nombres)

f = open ('nombres_2.txt','r')
nombres2 = ((f.read()).split("\nro1"))
f.close()
for index, nombre in enumerate(nombres2):
    nombres2[index] = ((nombre.replace(",","")))

print(nombres2)

nombresRepetidos = [nro1 for nro1 in nombres for nro2 in nombres2 if nro1 == nro2]
print("Nombres repetidos:", nombresRepetidos)

print("   {:<15} {:<10} {:<10} {:<10}".format("NOMBRE", "EVAL1", "EVAL2", "TOTAL"))
for i, estudiante in enumerate(zip(nombres, notas, notas2)):
    nombre, nota1, nota2 = estudiante
    nota1, nota2 = int(nota1), int(nota2)

    print(
        "{:<} {:<18} {:<10} {:<10} {:<10}".format(
            i, nombre, nota1, nota2, nota1 + nota2
        )
    )