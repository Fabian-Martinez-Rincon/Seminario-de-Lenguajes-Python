'''Styled sg elements.

Collection of helper functions to style sg elements that are common between screens.'''
from typing import Any

import PySimpleGUI as sg

from .. import constants
from ..controllers import theme


ImageFile = Any


def screen_title(
    title: str, spaced: bool = False, alignment: str = 'center',
    upper: bool = True, size: int = theme.H2_SIZE, padding: int = 0
) -> sg.Text:
    '''Generic screen title used on most screen.

    Args:
        title: String to display on screen generally the screen name
        spaced: whether the letters are spaced or close together , default is false
        alignment: default =  center
        upper: if is uper or lower case
        size: size of the font, default is H2
        padding: amount of padding
    Returns: 
        A sg.Text structured to use like a title.'''
    if upper:
        title = title.upper()
    if spaced:
        title = ' '.join(list(title.strip()))
    return sg.Text(
        title,
        size=(len(title), 1),
        background_color=theme.BG_BASE,
        text_color=theme.TEXT_ACCENT,
        font=(theme.FONT_FAMILY, size),
        justification=alignment,
        pad=padding if padding else (size//3)*2,
        expand_x=True
    )


def navigation_button(
    text: str, screen_name: str, font_size: int = theme.T1_SIZE,
    padding: tuple[int, int] = (0, 0), border: int = theme.BD_PRIMARY, disabled: bool = False
) -> sg.Button:
    '''Create a generic navigation button.

    Args:
        text: text displayed on the button
        screen_name: screen name to go
        font_size: default is T1
        padding: amount of padding default is 0,0
        border: size of border default is primary.
    Returns 
        A button with the style, theme and function applied.'''
    return sg.Button(
        text,
        disabled=disabled,
        key=f'{constants.GOTO_SCREEN} {screen_name}',
        font=(theme.FONT_FAMILY, font_size),
        button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border,
        pad=padding
    )


def goback_button(text: str, font_size: int = theme.H4_SIZE, padding: tuple[int, int] = (0, 0)) -> sg.Button:
    '''Create the generic back button.

    This buttons allows you back to the last screen.

    Args:
        text: text displayed on the button
        font_size: default is H4
        padding: default is (0,0)
    Returns 
        A button with the style, theme and function applied.'''
    return navigation_button(text, constants.LAST_SCREEN, font_size, padding)


def image_button(image: ImageFile, size: tuple[int, int], key: str, border: int = theme.BD_PRIMARY, padding: int = 0) -> sg.Button:
    '''Create generic Image Button.

    Args:
        image: image displayed on the button.
        size: size of the button
        key: key to refer the button
        border: border size, default: BD_PRIMARY.
        padding: amount of padding , default: 0
    Returns: 
        A Image button with the style theme applied.'''
    return sg.Button(
        key=key,
        image_size=size,
        image_subsample=(image.size//max(size)),
        image_data=image.source,
        auto_size_button=True,
        button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
        pad=padding,
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border
    )
