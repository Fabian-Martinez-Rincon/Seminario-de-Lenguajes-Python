notas = [ 4, 6, 7, 3, 8, 1, 10, 4]
total = 0

for i in range((len(notas))):
    print(notas[i])
    total += notas[i]
promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)

debajo_promedio = 0
for i in range((len(notas))):
    if notas[i] < promedio:
        debajo_promedio+=+1

print("La cantidad de alumnos con la nota por debajo del promedio es: ", debajo_promedio)