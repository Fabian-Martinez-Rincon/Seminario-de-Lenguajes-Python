from typing import Any

import PySimpleGUI as sg

from .. import default
from . import file


SCREEN_SIZE = sg.Window.get_screen_size()

HEIGHT_FACTOR_TABLE = {
    2160: 2.0,
    1440: 1.3,
    1080: 1.0,
    720: 0.7,
    480: 0.4
}

for height in HEIGHT_FACTOR_TABLE:
    if SCREEN_SIZE[1] >= height:
        screen_factor = HEIGHT_FACTOR_TABLE[height]
        break
else:
    screen_factor = 0.2


def apply_scale(value: int) -> int:
    '''Scale a value to fit the user's screen.'''
    return round(value * screen_factor)


class Theme:
    '''Class that contains GUI theming resources.'''

    def __init__(self, definition: dict[str, Any]) -> None:
        self.BG_BASE = definition['BG_BASE']
        self.BG_PRIMARY = definition['BG_PRIMARY']
        self.BG_SECONDARY = definition['BG_SECONDARY']

        self.BG_POPUP = definition['BG_POPUP']

        self.BG_BUTTON = definition['BG_BUTTON']
        self.BG_BUTTON_DISABLED = definition['BG_BUTTON_DISABLED']
        self.BG_BUTTON_HOVER = definition['BG_BUTTON_HOVER']

        self.TEXT_ACCENT = definition['F_C_ACCENT']
        self.TEXT_PRIMARY = definition['F_C_PRIMARY']
        self.TEXT_SECONDARY = definition['F_C_SECONDARY']

        self.TEXT_BUTTON = definition['F_C_BUTTON']
        self.TEXT_BUTTON_DISABLED = definition['F_C_BUTTON_DISABLED']
        self.TEXT_BUTTON_HOVER = definition['F_C_BUTTON_HOVER']

        self.BD_ACCENT = apply_scale(definition['BD_ACCENT'])
        self.BD_PRIMARY = apply_scale(definition['BD_PRIMARY'])
        self.BD_SECONDARY = apply_scale(definition['BD_SECONDARY'])
        self.BD_DELIMITER = apply_scale(definition['BD_DELIMITER'])

        self.FONT_FAMILY = definition['F_F_UI']
        self.FONT_FAMILY_TEXT = definition['F_F_CONTENT']

        self.H1_SIZE = apply_scale(definition['F_SIZE_H1'])
        self.H2_SIZE = apply_scale(definition['F_SIZE_H2'])
        self.H3_SIZE = apply_scale(definition['F_SIZE_H3'])
        self.H4_SIZE = apply_scale(definition['F_SIZE_H4'])
        self.T1_SIZE = apply_scale(definition['F_SIZE_T1'])
        self.T2_SIZE = apply_scale(definition['F_SIZE_T2'])
        self.T3_SIZE = apply_scale(definition['F_SIZE_T3'])

        self.BG_ERROR_ACCENT = definition['ERROR_BG_ACCENT']
        self.BG_ERROR_NORMAL = definition['ERROR_BG_NORMAL']
        self.BG_ERROR_SOFT = definition['ERROR_BG_SOFT']

    @property
    def height(self) -> int:
        '''Height in px of the user's screen.'''
        return SCREEN_SIZE[1]

    @property
    def width(self) -> int:
        '''Width in px of the user's screen.'''
        return SCREEN_SIZE[0]

    def scale(self, value: int) -> int:
        '''Scale a value to fit the user's screen.'''
        return apply_scale(value)


class ThemeController:
    '''Class for controlling application theming.'''

    def __init__(self, themes_path: str, default_theme: str) -> None:
        '''Tries to load the saved themes if it fails, loads from default themes.
        Also sets the application theme.

        Args:
            themes_path: absolute json file path of saved themes.
            default_theme: the application theme.'''
        self._raw_themes: dict[str, Any] = file.load_json(
            themes_path, default.THEMES
        )
        self._current_theme = default_theme if default_theme in self._raw_themes else list(self._raw_themes.keys())[0]
        self._theme = Theme(self._raw_themes[self._current_theme])

    @property
    def theme(self) -> Theme:
        return self._theme

    @property
    def theme_name(self) -> str:
        return self._current_theme

    @property
    def theme_list(self) -> list[str]:
        '''List of available themes.'''
        return [name for name in self._raw_themes]
