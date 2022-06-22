'''Contains global constants of the application.'''
import os.path

PATH_SRC = os.path.dirname(__file__)

PATH_SAVES = os.path.join(PATH_SRC, 'database', 'saves')
PATH_SETTINGS = os.path.join(PATH_SAVES, 'settings.json')
PATH_DIFFICULTIES = os.path.join(PATH_SAVES, 'difficulties.json')
PATH_THEME = os.path.join(PATH_SAVES, 'themes.json')
PATH_USERS = os.path.join(PATH_SAVES, 'users.json')

PATH_EVENTS = os.path.join(PATH_SRC, 'database', 'events')
PATH_DATASETS = os.path.join(PATH_SRC, 'database', 'datasets')
PATH_SCREENS = os.path.join(PATH_SRC, 'screens')

TIMEOUT = '-TIME-OUT-'
GOTO_VIEW = '-GOTO-VIEW-'
LAST_SCREEN = '-LAST-SCREEN-'
EXIT_APPLICATION = '-EXIT-APPLICATION-'
USER_CHANGE = '-USER-CHANGE-'
UPDATE_TIMEOUT = '-UPDATE-TIMEOUT-'
RUN_EVENT = '-RUN-EVENT-'
RUN_RESULT = '-RUN-RESULT-'
