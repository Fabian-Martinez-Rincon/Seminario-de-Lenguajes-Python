from cmath import tan

tabla = {"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":5,"jx":8,"qz":10}

palabra = "tomate"
total = 0
for letra in palabra:
    for clave in tabla:
        if (clave.count(letra)):
            total+=tabla[clave]
print(total)