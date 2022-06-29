'''Screen PreGame.'''
from random import shuffle
from typing import Any

import PySimpleGUI as sg

from .. import translations
from ..controllers import observer, theme, cards_controller as cards_ctr, difficulty_controller as difficulty_ctr
from . import _common, _csg


SCREEN_NAME = '-CONFIGURE-GAME-'
CHANGE_DIFFICULT = '-CHANGE-DIFFICULT-'
CHANGE_DATASET = '-CHANGE-DATASET-'
NO_DATASETS = 'No hay Datasets'

_text_font = ('System', theme.H3_SIZE)
_padding = theme.width // 4


_cmb_difficulty = _common.styled_combo(
    ('Fácil', 'Intermedio', 'Difícil', 'Insano', 'Personalizada'),
    'Intermedio',
    font=_text_font,
    ch_width=15,
    emit_event=True,
    key=CHANGE_DIFFICULT,
    padding=(theme.scale(64), 0)
)


def load_datasets() -> list[str]:
    datasets: list[str] = []
    for data in cards_ctr.types_list:
        datasets.append(translations.DATASET_TO_ES[data])
    if len(datasets) > 1:
        datasets.append('Random')
    elif len(datasets) <= 0:
        datasets.append(NO_DATASETS)
    return datasets


def is_loaded():
    return not cards_ctr.no_datasets


datasets: list[str] = load_datasets()

_cmb_dataset = _common.styled_combo(
    datasets,
    datasets[-1],
    font=_text_font,
    ch_width=15,
    emit_event=is_loaded(),
    key=CHANGE_DATASET,
    padding=(theme.scale(64), 0)
)


def combo_boxes() -> list[Any]:
    """Generates a row with the combo boxes for the layout.

    Returns:
        A row/list of elements correctly structured for the layout."""
    return [
        _csg.horizontal_spacer(_padding, theme.BG_BASE),
        _cmb_difficulty,
        sg.Push(theme.BG_BASE),
        _cmb_dataset,
        _csg.horizontal_spacer(_padding, theme.BG_BASE)
    ]


def header() -> list[Any]:
    """Header of the layout.

    Header that specify the configuration that correspond to the respective columns.

    Returns:
        A list of elements correctly structured to use like a header of the columns."""
    return [
        _csg.horizontal_spacer(_padding, theme.BG_BASE),
        sg.Text(
            'ELEGIR DIFICULTAD', pad=((50, 0), (50, 0)),
            background_color=theme.BG_BASE, font=_text_font
        ),
        sg.Push(theme.BG_BASE),
        sg.Text(
            'ELEGIR DATASET', pad=((50, 0), (50, 0)),
            background_color=theme.BG_BASE, font=_text_font
        ),
        _csg.horizontal_spacer(_padding, theme.BG_BASE)
    ]


_difficulty_info = sg.Multiline(
    f"Tiempo por ronda : {difficulty_ctr.difficulty.time_per_round}\
            Q de Características : {difficulty_ctr.difficulty.characteristics_shown}\
            Rounds por juego : {difficulty_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {difficulty_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {difficulty_ctr.difficulty.points_bad_answer}",
    auto_size_text=True,
    disabled=True,
    size=(20, 5),
    font=_text_font,
    border_width=0,
    text_color=theme.TEXT_ACCENT,
    no_scrollbar=True,
    background_color=theme.BG_BASE,
    key='-DIFFCAR-',
    pad=((50, 0), (50, 0))
)

_btn_start = _common.navigation_button(
    'Empezar !', screen_name='-GAME-', padding=(theme.scale(64),)*2, disabled=not is_loaded(),
)


def build_text() -> list[Any]:
    """Creates the text with the current difficulty settings selected.

    Returns:
        The current difficulty information correctly placed on the layout."""
    return [
        _csg.horizontal_spacer(_padding, background_color=theme.BG_BASE),
        _difficulty_info
    ]


def layout() -> list[list[Any]]:
    """Layout of the configure game screen.

    Returns:
        A list with all the elements used on the layout."""
    layout = [
        [_csg.vertical_spacer(theme.scale(24), theme.BG_BASE)],
        header(),
        [_csg.vertical_spacer(theme.scale(48), theme.BG_BASE)],
        combo_boxes(),
        build_text(),
        [sg.VPush(background_color=theme.BG_BASE)],
        [
            _common.goback_button(
                'Menu Principal', padding=(theme.scale(64),)*2
            ),
            sg.Push(background_color=theme.BG_BASE),
            _btn_start
        ],
    ]
    return layout


def pop_up_layout():
    '''Pop up that was displayed if the datasets are deleted or his charge failed.'''
    return [
        [sg.Text(
            'No hay datasets cargados \nIntente descargarlos y ubicarlos en src/database/datasets ',
            font=(theme.FONT_FAMILY, theme.T1_SIZE),
            text_color=theme.TEXT_ACCENT,
            background_color=theme.BG_SECONDARY,
            justification='center'
        )],
        [
            sg.Push(background_color=theme.BG_SECONDARY),
            sg.Button(
                button_text='Aceptar', k='-OK-',
                font=(theme.FONT_FAMILY, theme.T2_SIZE),
                border_width=theme.BD_SECONDARY, pad=theme.scale(20),
                button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON)
            ),
            sg.Push(background_color=theme.BG_SECONDARY)
        ]
    ]


def refresh_info() -> None:
    """Refresh the information displayed on screen of the current difficulty."""
    _cmb_difficulty.update(
        value=translations.DIFFICULTY_TO_ES[difficulty_ctr.difficulty_name]
    )
    difficulty_ctr.set_difficulty(
        translations.DIFFICULTY_TO_EN[_cmb_difficulty.get()]
    )
    _difficulty_info.update(
        f"Tiempo por ronda : {difficulty_ctr.difficulty.time_per_round}\
            Q de Características : {difficulty_ctr.difficulty.characteristics_shown}\
            Rounds por juego : {difficulty_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {difficulty_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {difficulty_ctr.difficulty.points_bad_answer}"
    )


def change_difficult() -> None:
    """Change the difficulty to the one selected in the difficulty combo box."""
    difficulty_ctr.set_difficulty(
        translations.DIFFICULTY_TO_EN[_cmb_difficulty.get()]
    )
    refresh_info()


def change_dataset() -> None:
    """Change the dataset to the one selected in the dataset combo box."""
    dataset = _cmb_dataset.get()
    if dataset == NO_DATASETS:
        return
    if dataset == 'Random':
        shuffled = cards_ctr.types_list
        shuffle(shuffled)
        dataset = shuffled[0]
    else:
        dataset = translations.DATASET_TO_EN[dataset]
    cards_ctr.type = dataset


observer.subscribe(CHANGE_DIFFICULT, change_difficult)
observer.subscribe(CHANGE_DATASET, change_dataset)


screen_layout = [
    [_common.screen_title(
        'CONFIGURAR JUEGO', alignment='left', padding=theme.height//64
    )],
    [sg.Column(
        layout(), background_color=theme.BG_BASE, expand_y=True,
        expand_x=True, justification='right'
    )],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c',
}


def screen_reset() -> None:
    """Updates the information when entered to the screen."""
    refresh_info()
    datasets = load_datasets()
    _cmb_dataset.update(datasets[-1], datasets)
    _btn_start.update(disabled=not is_loaded())
    if not is_loaded():
        _csg.custom_popup(
            pop_up_layout(), background_color=theme.BG_SECONDARY
        )
    change_dataset()
