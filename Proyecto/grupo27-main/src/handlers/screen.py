import importlib
import os
from dataclasses import dataclass
from typing import Any, Callable

import PySimpleGUI as sg

from .. import constants
from . import observer, file


@dataclass
class NotRegisteredScreenError(Exception):
    screen_name: str


@dataclass
class DuplicatedScreenError(Exception):
    screen_name: str


class Screen:
    '''Class that models an application screen.'''

    def __init__(self, key: str, layout: list[list[Any]], config: dict[str, Any], reset: Callable[..., None]) -> None:
        '''Initializes the screen object.

        Args:
            key: the screen name.
            layout: the composition of the screen, like a sg.Window layout.
            config: configuration dictionary, items must be like sg.Column arguments.
            reset: function to execute each time this screen becomes visible.'''
        config['key'] = key
        config['visible'] = False
        config['expand_x'] = True
        config['expand_y'] = True
        config['pad'] = 0
        self.key = key
        self.is_visible = False
        self.container = sg.Column(layout, **config)
        self._reset = reset

    def toggle_visivility(self) -> None:
        '''Change the visibility status of the screen.

        If the screen becomes visible, executes its reset function.'''
        self.is_visible = not self.is_visible
        self.container.update(visible=self.is_visible)
        if self.is_visible:
            self._reset()


class ScreenController:
    '''Class for controlling application screens.'''

    def __init__(self, screens_folder_path: str) -> None:
        '''Initialize and register all the screen modules from the given path.

        Args:
            screens_folder_path: absolute directory path of screen modules.'''
        self._current_screen: str = ''
        self._screen_stack: list[str] = []
        self._screens: dict[str, Screen] = {}
        self._composed_layout: list[Any] = []

        path_names = screens_folder_path.split(os.path.sep)
        base_to_folder = path_names[path_names.index('src'):]
        for file_name, _ in file.scan_dir(screens_folder_path, 'py'):
            if file_name.startswith('_'):
                continue
            names = base_to_folder + [file_name.split('.')[0]]
            module = importlib.import_module('.'.join(names))
            self._register(Screen(
                module.SCREEN_NAME,
                module.screen_layout,
                module.screen_config,
                module.screen_reset
            ))
        observer.subscribe(constants.GOTO_SCREEN, self._goto_layout)

    def _goto_layout(self, key: str) -> None:
        '''Change the view from one screen to another.

        Args:
            key: the screen name or keyword related to screen navigation.'''
        key = key.rstrip('0123456789')
        self._screens[self._current_screen].toggle_visivility()
        if key == constants.LAST_SCREEN:
            self._current_screen = self._screen_stack.pop()
        elif key in self._screen_stack:
            while self._screen_stack.pop() != key:
                continue
            self._current_screen = key
        else:
            self._screen_stack.append(self._current_screen)
            self._current_screen = key

        self._screens[self._current_screen].toggle_visivility()

    def _register(self, screen: Screen) -> None:
        '''Registers a screen.

        Args:
            screen: the screen instance to be registered.
        Raises:
            DuplicatedScreenError: the screen is already registered.'''
        if screen.key in self._screens:
            raise DuplicatedScreenError(screen.key)
        self._screens[screen.key] = screen
        self._composed_layout.append(screen.container)

    def is_registered(self, screen_name: str) -> bool:
        return screen_name in self._screens

    def init(self, screen_name: str) -> None:
        '''Initilize the starting screen.

        Args:
            screen_name: the screen name to be made visible.
        Raises:
            NotRegisteredScreenErrror: the screen name isnt registered.'''
        if screen_name not in self._screens:
            raise NotRegisteredScreenError(screen_name)
        self._current_screen = screen_name
        self._screens[screen_name].toggle_visivility()

    @property
    def composed_layout(self) -> list[list[Any]]:
        '''The layout containing all the registered screens.'''
        return [self._composed_layout]
