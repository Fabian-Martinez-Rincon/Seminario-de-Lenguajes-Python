tabla = {"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":5,"jx":8,"qz":10}

palabra = "tomate"
total = 0
for letra in palabra:
    if letra in tabla:
        total+=tabla[letra]* letra.count(letra)
print(total)
#Accedo directo
#tratar de usar filter
#yield 