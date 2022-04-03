from lib2to3.pgen2.token import EQUAL
import os
clear = lambda: os.system('cls')
clear()

archivo = open("./Practicas/Practica2/readme.txt","r")
lineas = archivo.read().rstrip().split("\n")
links = []
for linea in lineas:
    if ("https" in linea)  :
        links.append(linea)

print(*links,sep = "\n",end="\nGIGI")