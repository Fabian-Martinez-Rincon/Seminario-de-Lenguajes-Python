# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
def Imprimir(linesFile:list[str]):
    for line in linesFile:
        print (line)
file = open('nuevoArchivo.txt')
linesFile = file.readlines()

menu = ConsoleMenu("Title", "Subtitle")

menu_item = MenuItem(Imprimir(linesFile))

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)


file.close()
# Finally, we call show to show the menu and allow the user to interact
menu.show()

