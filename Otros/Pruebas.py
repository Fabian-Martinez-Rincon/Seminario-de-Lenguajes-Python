def Ingresar(lista_de_notas:list[int]):
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
    
    while nota != -1:
        lista_de_notas.append(nota)
        nota = int(input("Ingresá una nota (-1 para finalizar)"))
    return lista_de_notas

lista_de_notas:list[int] = []
lista_de_notas=Ingresar(lista_de_notas)
print(lista_de_notas)