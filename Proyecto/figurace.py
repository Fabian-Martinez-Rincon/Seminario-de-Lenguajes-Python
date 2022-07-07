'''Entry point of the application.'''
import sys

from src import main


args = sys.argv[1:]

if not args or args[0] != '--dev':
    main.main()
else:
    main.main_dev(args[1:])
