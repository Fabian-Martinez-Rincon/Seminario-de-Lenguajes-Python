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
    def __init__(self, key: str, layout: list[list[Any]], config: dict[str, Any], reset: Callable[..., None]) -> None:
        config['key'] = key
        config['visible'] = False
        config['expand_x'] = True
        config['expand_y'] = True
        config['pad'] = 0
        self.key = key
        self.is_visible = False
        self.container = sg.Column(layout, **config)
        self._reset = reset

    def turn_visivility(self) -> None:
        self.is_visible = not self.is_visible
        self.container.update(visible=self.is_visible)
        if self.is_visible:
            self.reset()

    def reset(self) -> None:
        self._reset()


class ScreenController:
    def __init__(self, screens_folder_path: str) -> None:
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
        observer.subscribe(constants.GOTO_VIEW, self._goto_layout)

    def _goto_layout(self, key: str) -> None:
        key = key.rstrip('0123456789')
        self._screens[self._current_screen].turn_visivility()
        if key == constants.LAST_SCREEN:
            self._current_screen = self._screen_stack.pop()
        elif key in self._screen_stack:
            while self._screen_stack.pop() != key:
                continue
            self._current_screen = key
        else:
            self._screen_stack.append(self._current_screen)
            self._current_screen = key

        self._screens[self._current_screen].turn_visivility()

    def _register(self, screen: Screen) -> None:
        if screen.key in self._screens:
            raise DuplicatedScreenError(screen.key)
        self._screens[screen.key] = screen
        self._composed_layout.append(screen.container)

    def is_registered(self, screen_name: str) -> bool:
        return screen_name in self._screens

    def init(self, screen_name: str) -> None:
        if screen_name not in self._screens:
            raise NotRegisteredScreenError(screen_name)
        self._current_screen = screen_name
        self._screens[screen_name].turn_visivility()

    @property
    def composed_layout(self) -> list[list[Any]]:
        return [self._composed_layout]
