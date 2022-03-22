notas = {"Janis Joplin":10, "Elvis Presley": 9, "Bob Marley": 5, "Jimi Hendrix": 9}
notas["Bob Marley"]
total = 0


for key in notas:
    print (key, ":", notas[key])
    total += notas[key]

promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)
debajo_promedio = 0
for i in notas:
    if notas[i] < promedio:
        print("El estudiantes", i , "Esta por debajo del promedio")
        debajo_promedio+=+1
