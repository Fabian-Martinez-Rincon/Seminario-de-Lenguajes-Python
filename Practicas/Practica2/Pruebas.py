f = open ('nombres_3.txt','r')
notas = ((f.read()).split("\n"))
f.close()
for index, nota in enumerate(notas):
    notas[index] = ((nota.replace(",","")))
print(notas)