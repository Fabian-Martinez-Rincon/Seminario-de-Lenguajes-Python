'''Formulary needed to create a new profile.'''
from typing import Callable, TypedDict

import PySimpleGUI as sg

from ..controllers import observer, theme, users_controller as users_ctr
from . import _common, _csg


SCREEN_NAME = '-CREATE-USER-'
LOAD_USER_FIELD = '-LOAD-USER-FIELD-'
EVENT_ADD_PROFILE = '-ADD-PROFILE-'


class FormInput(TypedDict):
    '''Defines the data structure of an input for its logical handling.'''
    input: sg.Input
    state: bool
    validate_fn: Callable[[sg.Input], bool]


def create_input(key: str) -> sg.Input:
    '''
    Returns: 
        A input with your own key and design.'''
    return sg.Input(
        size=(20, 1),
        background_color=theme.BG_BASE,
        font=(theme.FONT_FAMILY, theme.H3_SIZE),
        text_color=theme.TEXT_ACCENT,
        border_width=theme.BD_SECONDARY,
        key=f'{LOAD_USER_FIELD} {key}',
        enable_events=True
    )


def validate_nick(input: sg.Input) -> bool:
    '''Make sure the input nick field is completed correctly.'''
    nick = input.get()
    if nick == '' or nick in users_ctr.transform_users(lambda user: user.nick):
        input.update(background_color=theme.BG_ERROR_NORMAL)
        return False
    input.update(background_color=theme.BG_BASE)
    return True


def validate_age(input: sg.Input) -> bool:
    '''Make sure the input age field is completed correctly.'''
    age = input.get()
    try:
        age = int(age)
        if age <= 0 or age > 100:
            raise ValueError
    except ValueError:
        input.update(background_color=theme.BG_ERROR_NORMAL)
        return False
    input.update(background_color=theme.BG_BASE)
    return True


def validate_gender(input: sg.Input) -> bool:
    '''Make sure the input field is completed correctly.'''
    gender = input.get()
    if gender == '':
        input.update(background_color=theme.BG_ERROR_NORMAL)
        return False
    input.update(background_color=theme.BG_BASE)
    return True


FORMULARY_FIELDS = (
    ('nick', validate_nick),
    ('age', validate_age),
    ('gender', validate_gender),
)

inputs: dict[str, FormInput] = {}

for type, validation_fn in FORMULARY_FIELDS:
    inputs[type] = {
        'input': create_input(type),
        'state': False,
        'validate_fn': validation_fn
    }

create_button = sg.Button(
    'Crear',
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.H4_SIZE),
    pad=theme.scale(32),
    disabled=True,
    key=EVENT_ADD_PROFILE,
    border_width=theme.BD_PRIMARY
)


def disable_create_button() -> None:
    create_button.update(
        disabled=True,
        button_color=(theme.TEXT_BUTTON_DISABLED, theme.BG_BUTTON_DISABLED)
    )


def enable_create_button() -> None:
    create_button.update(
        disabled=False,
        button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON)
    )


def create_field(name: str, input: sg.Input) -> tuple[sg.Text, sg.Input]:
    '''Creates a field for a formulary.'''
    return (
        sg.Text(
            name,
            size=(6, 1),
            background_color=theme.BG_BASE,
            font=(theme.FONT_FAMILY, theme.H3_SIZE),
            pad=theme.scale(25)
        ),
        input
    )


def create_formulary() -> sg.Column:
    '''Create the structure of the formulary.

    Returns: 
        The layout within a centered column.'''
    layout = [
        [*create_field('Nick', inputs['nick']['input'])],
        [*create_field('Edad', inputs['age']['input'])],
        [*create_field('Género', inputs['gender']['input'])],
        [
            sg.Push(theme.BG_BASE),
            create_button,
            sg.Push(theme.BG_BASE)
        ]
    ]

    return _csg.centered(layout, background_color=theme.BG_BASE)


def reset_formulary() -> None:
    '''Reset the form to its default state.'''
    for value in inputs.values():
        value['input'].update('', background_color=theme.BG_BASE)
        value['state'] = False
    disable_create_button()


def validate_inputs(key: str) -> None:
    '''Validates input and update the state of the create button.

    Args: 
        key: key of the formulary to validate.'''
    inputs[key]['state'] = inputs[key]['validate_fn'](inputs[key]['input'])

    for input in inputs.values():
        if not input['state']:
            disable_create_button()
            break
    else:
        enable_create_button()


observer.subscribe(LOAD_USER_FIELD, validate_inputs)


def create_user() -> None:
    '''A new profile is created and informed by a popup.'''
    nick: str = inputs['nick']['input'].get()
    users_ctr.add(
        nick,
        int(inputs['age']['input'].get()),
        inputs['gender']['input'].get()
    )
    reset_formulary()
    _csg.custom_popup(
        [
            [sg.Text(
                f'Perfil {nick}\ncreado exitosamente',
                font=(theme.FONT_FAMILY, theme.T1_SIZE),
                text_color=theme.TEXT_ACCENT,
                background_color=theme.BG_SECONDARY,
                pad=theme.scale(32),
                justification='center'
            )],
        ],
        background_color=theme.BG_SECONDARY,
        duration=2
    )


observer.subscribe(EVENT_ADD_PROFILE, create_user)


screen_layout = [
    [_common.screen_title('crear perfil', True)],
    [create_formulary()],
    [_common.goback_button('Menu Selección', padding=(theme.scale(64),)*2)],
]

screen_config = {
    'background_color': theme.BG_BASE,
}


def screen_reset() -> None:
    '''Reset the screen content to a default/updated state.'''
    reset_formulary()
