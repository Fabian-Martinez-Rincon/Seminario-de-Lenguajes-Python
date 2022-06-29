'''Punto de entrada de la aplicación.'''
import sys

from src import main


args = sys.argv[1:] # Accedemos a los argumentos pasados por marametro (sin contar el nombre)
# Ej py figurace.py


if not args or args[0] != '--dev': # Si no tenemos argumentos o es distinto que --dev
    main.main()
else:
    main.main_dev(args[1:])
