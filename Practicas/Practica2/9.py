celdas = [
'-*-*-',
'--*--',
'----*',
'*----'
]
celdas = [list(col) for col in celdas]
def GuardarNumero(fila, columna):
    cant = 0

    Empieza_Fila = 0 if fila == 0 else -1
    Termina_Fila = 1 if fila == 3 else 2

    Empieza_Columna = 0 if columna == 0 else -1
    Termina_Columna = 1 if columna == 4 else 2

    for i in range(Empieza_Fila, Termina_Fila):
        for j in range(Empieza_Columna, Termina_Columna):
            if celdas[fila + i][columna + j] == "*":
                cant += 1
    return cant



x = 0
y = 0
print(celdas)
celdas_bombas = []
print("_"*30)
print("Las siguientes celdas tienen bombas")
for celda in celdas:
    x = 0
    for bomba in celda:
        if (bomba=="-"):
            celdas[y][x] = GuardarNumero(y,x)
            celdas_bombas.append([y,x])
            #print("La celda [", y,"],[",x,"] ")
        x+=1
    y+=1
#Pattern Matching 
print("_"*30)
print(celdas_bombas)

print(celdas)