f = open ('eval1.txt','r')
notas = ((f.read()).split("\n"))
f.close()
for index, nota in enumerate(notas):
    notas[index] = ((nota.replace(",","")))

notas.pop(-1) #Elimine el ultimo elemento ya que no me dejaba convertirlos porque era un string
int_list = list(map(int, notas))

f = open ('eval2.txt','r')
notas2 = ((f.read()).split("\n"))
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
nombres = ((f.read()).split("\n"))
f.close()
for index, nombre in enumerate(nombres):
    nombres[index] = ((nombre.replace(",","")))

print(nombres)

dict_from_list = dict(zip(nombres,nuevasNotas ))
print(dict_from_list)

promedio = sum(nuevasNotas) / len(nuevasNotas)
print(promedio)



for clave, valor in dict_from_list.items():
    if valor> promedio:
        print(clave)