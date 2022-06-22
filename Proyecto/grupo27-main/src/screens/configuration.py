'''Configuration Screen.'''
from typing import Any

import PySimpleGUI as sg

from ..controllers import observer, theme, difficulty_controller as difficulty_ctr, users_controller as user_ctr
from . import _common, _csg


SCREEN_NAME = "-CONFIGURATION-"
default_padding = 8
_font = (theme.FONT_FAMILY_TEXT, theme.T1_SIZE)
_padding = theme.width // 8


def build_text(text: str, unit: str, combo: sg.Combo) -> list[Any]:
    """Build a Text with his Combo editable .

    Put the text and the combo spaced correctly and specify the unit that operate the combo.

    Args:
        text : the description of the combo editable 
        unit : unit that operate the combo
        combo : combo displayed on screen

    Returns:
        A list of elements with the arguments structured.

    """
    result = [
        _csg.horizontal_spacer(theme.width//16,
                              background_color=theme.BG_BASE),
        sg.Multiline(text,
                     disabled=True,
                     justification='left',
                     size=(25, 1),
                     font=_font,
                     text_color=theme.TEXT_ACCENT,
                     no_scrollbar=True,
                     background_color=theme.BG_BASE,
                     border_width=0,),
        _csg.horizontal_spacer(theme.width//16,
                              background_color=theme.BG_BASE),
        sg.Text(unit, background_color=theme.BG_BASE),
        combo, ]
    return result


_cmb_time_per_game = sg.Combo(
    ('15', '30', '60', '90', '180', '300'),
    difficulty_ctr.difficulty.time_per_round,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    size=(3, 1),
    readonly=True,
    key='-TIME-',)

_cmb_features_per_level = sg.Combo(
    ('1', '2', '3', '4', '5'),
    difficulty_ctr.difficulty.characteristics_shown,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-CARXLEVEL-')

_cmb_rounds_per_game = sg.Combo(
    ('3', '5', '8', '10', '20'),
    difficulty_ctr.difficulty.rounds_per_game,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-QROUNDS-')

_cmb_plus_points = sg.Combo(
    ('1', '5', '10', '25', '50'),
    difficulty_ctr.difficulty.points_correct_answer,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-+QXANSWER-')

_cmb_sub_points = sg.Combo(
    ('-1', '-5', '-10', '-25', '-50'),
    difficulty_ctr.difficulty.points_bad_answer,
    background_color=theme.BG_BUTTON,
    font=_font,
    text_color=theme.BG_BASE,
    readonly=True,
    size=(3, 1),
    key='--QXANSWER-')

_btn_save = sg.Button(
    'Guardar Dificultad', size=(16, 1),
    key='-SAVE-DIFF-CUSTOM-',
    font=('System', theme.H3_SIZE),
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    pad=default_padding,
    mouseover_colors=theme.BG_BUTTON_HOVER,
    border_width=theme.BD_PRIMARY)


_input_nick = sg.Multiline(user_ctr.current_user.nick,
                           size=(20, 1),
                           disabled=True,
                           no_scrollbar=True,
                           background_color=theme.BG_BASE,
                           font=_font,
                           text_color=theme.TEXT_ACCENT,
                           border_width=theme.BD_PRIMARY,
                           enable_events=True
                           )

_input_age = sg.Input(default_text=user_ctr.current_user.age,
                      size=(20, 1),
                      background_color=theme.BG_BASE,
                      font=_font,
                      text_color=theme.TEXT_ACCENT,
                      border_width=theme.BD_PRIMARY,
                      key='-AGE-',
                      enable_events=True
                      )

_input_gender = sg.Input(default_text=user_ctr.current_user.gender,
                         size=(20, 1),
                         background_color=theme.BG_BASE,
                         font=_font,
                         text_color=theme.TEXT_ACCENT,
                         border_width=theme.BD_PRIMARY,
                         key='-GENDER-',
                         enable_events=True
                         )


_btn_edit = sg.Button(
    'Actualizar Usuario',
    key='-EDIT-USER-',
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.T1_SIZE),
    border_width=theme.BD_ACCENT
)


def header() -> list[Any]:
    """Header that specifies the columns info.

    Returns:
        A row of elements that specifies the configurations columns used on the screen.
    """
    return [
        _csg.horizontal_spacer(_padding,
                              background_color=theme.BG_BASE),
        sg.Text('DIFICULTAD PERSONALIZADA', pad=((50, 0), (20, 0)),
                background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
        sg.Push(background_color=theme.BG_BASE),
        sg.Text('EDITAR USUARIO', pad=((50, 0), (20, 0)),
                background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
        _csg.horizontal_spacer(_padding,
                              background_color=theme.BG_BASE)
    ]


def textv_spacer() -> list[Any]:
    """Generic vertical Spacer
    Returns: 
        a list with a vertical spacer proportionally to the screen size
    """
    return [_csg.vertical_spacer(theme.height//92, background_color=theme.BG_BASE)]


def texth_spacer() -> sg.Column:
    """Generic horizontal Spacer
    Returns: 
        a list with a horizontal spacer proportionally to the screen size
    """
    return _csg.horizontal_spacer(theme.width//6, background_color=theme.BG_BASE)


def text_input(text: str) -> sg.Text:
    """Text specifying  the input needed

    Args:
        text : text displayed for specified  the input
    Returns: 
        the argument with the theme applied as a sg.Text.
    """
    return sg.Text(text,
                   size=(6, 1),
                   background_color=theme.BG_BASE,
                   font=_font,
                   pad=theme.scale(25)
                   )


def config_layout() -> list[list[Any]]:
    """Generate layout
    Structured menu options on a function that return the layout needed to display on window.

    Returns:
        Layout used on the screen
    """
    config_layout = [
        header(),
        [_csg.vertical_spacer(
            theme.height//16, background_color=theme.BG_BASE)],

        [*build_text('Tiempo por ronda', 'Segundos:',
                     _cmb_time_per_game),
         texth_spacer(),
         text_input('Nick'),
         _input_nick],
        textv_spacer(),

        [*build_text('Características por nivel',
                     'Cantidad:  ', _cmb_features_per_level,),
         texth_spacer(),
         text_input('Edad'),
         _input_age],
        textv_spacer(),

        [*build_text('Rondas por juego', 'Cantidad:  ',
                     _cmb_rounds_per_game),
         texth_spacer(),
         text_input('Género'),
         _input_gender],
        textv_spacer(),

        [*build_text('Puntos añadidos ', 'Cantidad:  ',
                     _cmb_plus_points),
         texth_spacer(),
         _csg.horizontal_spacer(theme.scale(
             100), background_color=theme.BG_BASE),
         _btn_edit,
         _csg.horizontal_spacer(theme.scale(80), background_color=theme.BG_BASE)],
        textv_spacer(),

        build_text('Puntos restados', 'Cantidad:  ', _cmb_sub_points),
        textv_spacer(),

        [_common.goback_button('<--'),
            _csg.horizontal_spacer(theme.scale(
                200), background_color=theme.BG_BASE),
         _btn_save, ]
    ]

    return config_layout


def validate_age() -> bool:
    """ 
        Validate if the age writen on the input_age is between 0 and 100

        Returns: 
            If the age is correctly writen on the input
    """
    age = _input_age.get()
    try:
        age = int(age)
        if age <= 0 or age > 100:
            raise ValueError
    except ValueError:
        _input_age.update(background_color='Red')
        return False
    _input_age.update(background_color=theme.BG_BASE,)
    return True


def validate_gender():
    """
        Validate if the gender writen on the _input_gender its not empty

        Returns:
            If the gender is correctly writen on the input
    """
    gender = _input_gender.get()
    if gender == '':
        _input_gender.update(background_color='red')
        return False
    _input_gender.update(background_color=theme.BG_BASE,)
    return True


def validate_all() -> None:
    """
        Validate all inputs are put correctly
    """
    result = validate_gender() + validate_age()
    _btn_edit.update(disabled=result != 2)


def save_settings() -> None:
    """ Save the custom difficulty configuration put on the combos

    Check all the combos and with the help of the controllers update on the JSON the custom difficulty.
    """
    changes = {
        'time_per_round': int(_cmb_time_per_game.get()),
        'rounds_per_game': int(_cmb_rounds_per_game.get()),
        'points_correct_answer': int(_cmb_plus_points.get()),
        'points_bad_answer':  int(_cmb_sub_points.get()),
        'characteristics_shown': int(_cmb_features_per_level.get())
    }
    difficulty_ctr.update_difficulty(**changes)


def update_user() -> None:
    """Updates the user with the information put in the inputs widgets.

    """
    user_ctr.current_user.age = int(_input_age.get())
    user_ctr.current_user.gender = _input_gender.get()
    pass


def refresh_inputs() -> None:
    """Puts in the inputs widgets the information of the current user 

    """
    _input_nick.update(value=user_ctr.current_user.nick)
    _input_age.update(value=str(user_ctr.current_user.age))
    _input_gender.update(value=user_ctr.current_user.gender)


screen_layout = [
    [_common.screen_title('Configuración', spaced=True, alignment='center')],
    [sg.Column(config_layout(), background_color=theme.BG_BASE, expand_x=True)],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center'
}


def screen_reset():
    """Refresh information for the current user and current custom difficulty"""
    refresh_inputs()
    # refresh_difficulty()
    pass


observer.subscribe(
    '-AGE-',
    validate_all
)
observer.subscribe(
    '-GENDER-',
    validate_all
)
observer.subscribe(
    '-EDIT-USER-',
    update_user
)
observer.subscribe(
    '-SAVE-DIFF-CUSTOM-',
    save_settings,
)
