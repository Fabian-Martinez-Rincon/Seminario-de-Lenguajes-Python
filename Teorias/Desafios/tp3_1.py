from typing import Any
def imprimo(*args:Any): #El tipo any es cualquier tipo
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")  

imprimo(1)
print("-"*30)
imprimo(2, "hola")
print("-"*30)
imprimo([1,2], "hola", 3.2)