from typing import Any

import PySimpleGUI as sg

from .. import constants as const
from ..controllers import observer, theme, users_controller as users_ctr
from . import _common, _csg


SCREEN_NAME = '-SELECT-PROFILE-'
EVENT_CREATE_PROFILE = '-CREATE-PROFILE-'
EVENT_REMOVE_PROFILE = '-REMOVE-PROFILE-'
EVENT_EDIT_PROFILE = '-EDIT-PROFILE-'
EVENT_ADD_PROFILE = '-ADD-PROFILE-'
LOAD_USER_FIELD = '-LOAD-FIELD-'


_play_button = sg.Button('-<-Jugar->-',
                         key=f'{const.GOTO_SCREEN} -MENU-',
                         border_width=theme.BD_ACCENT,
                         button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         font=(theme.FONT_FAMILY, theme.T1_SIZE),
                         disabled=True,
                         pad=(theme.scale(100), theme.scale(50))
                         )

_current_user = sg.Text('Seleccionado:',
                        background_color=theme.BG_BASE,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        size=(24, 1)
                        )

_user_list = sg.Listbox(values=users_ctr.users_transform(lambda user: user.nick),
                        expand_y=True,
                        size=(25, 10),
                        background_color=theme.BG_BASE,
                        no_scrollbar=True,
                        highlight_background_color=theme.BG_PRIMARY,
                        text_color=theme.TEXT_PRIMARY,
                        highlight_text_color=theme.TEXT_PRIMARY,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        enable_events = True,
                        key='-ENABLE-',
                        )

_remove_button = sg.Button(
    button_text='Eliminar',
    key='-REMOVE-PROFILE-',
    border_width=theme.BD_ACCENT,
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.T1_SIZE),
    disabled=True,
    pad=theme.scale(30),
    enable_events=True
)

_edit_button = _common.navigation_button(
    'Editar',
    '-CONFIGURATION-',
    border=theme.BD_ACCENT,
    padding=(theme.scale(30),)*2
)

_select_profile_layout = [
    [_current_user],
    [_user_list]
]

_button_layout = [
    [
        _common.navigation_button(
            'Crear',
            '-CREATE-PROFILE-',
            border=theme.BD_ACCENT,
            padding=(theme.scale(30),)*2,
        )
    ],
    [
        _edit_button
    ],
    [
        _remove_button
    ]

]

_play_layout = [
    [_play_button]
]

screen_layout = [
    [
        _common.screen_title('Seleccionar perfiles', alignment='center')
    ],
    [
        _csg.horizontal_spacer(width=theme.scale(
            500),
            background_color=theme.BG_BASE
        ),
        sg.Column(_select_profile_layout,
                  background_color=theme.BG_BASE,
                  element_justification='center',
                  justification='left',
                  expand_y=True,
                  pad=theme.scale(40)
                  ),
        _csg.horizontal_spacer(width=theme.scale(
            200),
            background_color=theme.BG_BASE
        ),
        sg.Column(
            _button_layout,
            justification='center',
            element_justification='center',
            background_color=theme.BG_BASE)
    ],
    [sg.Column(
        _play_layout,
        justification='center',
        expand_x=True,
        element_justification='center',
        background_color=theme.BG_BASE
    )
    ],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center'
}


def screen_reset() -> None:
    '''Refresh the information in the list of users and the selected.'''
    update_user_list()
    reset_select_user()


def enable_selection() -> None:
    """
    Enables user interaction buttons and show the selected one.
    """
    if len(_user_list.get_list_values()) == 0 :
        return
    _play_button.update(disabled=False)
    _remove_button.update(disabled=False)
    _edit_button.update(disabled=False)
    _current_user.update(f'Selecionado: {_user_list.get()[0]}', font=(
        theme.FONT_FAMILY, theme.H3_SIZE))
    users_ctr.current_user = _user_list.get()[0]

observer.subscribe('-ENABLE-', enable_selection)


def update_user_list() -> None:
    """
    Update the list of profiles.
    """
    _user_list.update(values = users_ctr.users_transform(lambda user: user.nick))


def reset_select_user() -> None:
    """ 
    Reset the selected user and disables the play buttons - delete and edit profiles.
    """
    _play_button.update(disabled=True)
    _remove_button.update(disabled=True)
    _edit_button.update(disabled=True)
    _current_user.update('Seleccionado: ')


def _new_popup_layout(popup_text: str = '') -> list[list[Any]]:
    """
    Args: 
        popup_text: text to display in the popup
    Returns: 
        The layout for a popup window to accept or cancel an action.
    """
    return [
        [
            sg.Text(
                popup_text, background_color=theme.BG_POPUP,
                text_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.T2_SIZE)
            )
        ],
        [
            sg.Button(
                button_text='Cancelar', k='-CANCEL-',
                font=(theme.FONT_FAMILY, theme.T2_SIZE),
                border_width=theme.BD_SECONDARY, pad=theme.scale(20),
                button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON)
            ),
            sg.Push(background_color=theme.BG_POPUP),
            sg.Button(
                button_text='Aceptar', k='-OK-',
                font=(theme.FONT_FAMILY, theme.T2_SIZE),
                border_width=theme.BD_SECONDARY, pad=theme.scale(20),
                button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON)
            ),
        ]
    ]


def remove() -> None:
    """Check if you really want to delete the profile, by means of a popup, when affirming , the selected profile is deleted.
    """
    response = _csg.custom_popup(
        _new_popup_layout('¿Deseas eliminar este usuario?'),
        close_keys=['-OK-', '-CANCEL-'],
        background_color=theme.BG_POPUP
    )
    if response == '-OK-':
        users_ctr.remove(_user_list.get()[0])
    screen_reset()


observer.subscribe('-REMOVE-PROFILE-', remove)
