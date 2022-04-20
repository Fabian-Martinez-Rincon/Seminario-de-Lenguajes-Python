import os

clear = lambda: os.system('cls')
clear()
archivo = open("readme.txt","r")
links = []
for linea in archivo:
    if ("https" in linea)  :
        links.append(linea)

print(links)
archivo.close()