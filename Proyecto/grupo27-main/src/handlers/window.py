'''Module for controlling application GUI.'''
from typing import Any

import PySimpleGUI as sg

from .. import constants
from . import observer, screen


class WindowController:
    '''Class for controlling sg.Window instance and main event loop.'''

    def __init__(self, screens_folder_path: str) -> None:
        '''Initializes the 'screens' that conform the application.

        Args:
            screens_folder_path: absolute path where screens modules are located.'''
        self._screen_ctr = screen.ScreenController(screens_folder_path)
        self._timeout: int | None = None
        self._timeout_key: str = constants.TIMEOUT
        observer.subscribe(constants.UPDATE_TIMEOUT, self.set_timeout)

    @property
    def screen_ctr(self) -> screen.ScreenController:
        return self._screen_ctr

    def set_timeout(self, duration: int | None = None, key: str = constants.TIMEOUT) -> None:
        '''Updates the timeout parameters for inactivity related to GUI.

        Args:
            duration: max time in miliseconds of inactivity.
            key: the type of event generated at timeout.'''
        self._timeout = duration
        self._timeout_key = key

    def init(self, initial_screen: str, title: str, app_icon: Any = None, fullscreen: bool = True) -> None:
        '''Initilize the application window.

        Args:
            initial_screen: the screen name for the starting screen.
            title: the name of the window.
            app_icon: the module containing the image for the application icon.
            fullscreen: True for fullscrren otherwise False.'''
        self._window = sg.Window(
            title,
            self._screen_ctr.composed_layout,
            icon=app_icon.source if app_icon else None,
            finalize=True,
            element_justification='center',
            resizable=True,
            margins=(0, 0)
        )

        if fullscreen:
            self._window.maximize()

        self._screen_ctr.init(initial_screen)

    def loop(self) -> None:
        '''Ejecuta el bucle de eventos principal y limpia correctamente los recursos al final..
        
        Raises:
            Exception: cualquier excepción inesperada en tiempo de ejecución.'''
        try:
            while True:
                event, _ = self._window.read(self._timeout, self._timeout_key)
                if event is None or event.startswith(constants.EXIT_APPLICATION):
                    break

                event_type, *event_data = event.split()
                observer.post_event(event_type, *event_data)
        except Exception as error:
            raise error
        finally:
            observer.post_event(constants.EXIT_APPLICATION)
            self._window.close()
