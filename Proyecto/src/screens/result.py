'''Summary for the result of a run.'''
import PySimpleGUI as sg

from .. import constants
from ..controllers import observer, theme
from . import _common, _csg


SCREEN_NAME = '-RESULT-'
FIELD_MAX_CHARACTERS = 32

summary: dict[str, sg.Text] = {}


def create_stat_type(text: str, width: int | None = None) -> sg.Text:
    ''' Create a description field for a stat.

    Args:
        text: the description of the field
        width: the length required for the field.
    Returns:
        A descriptive text with the theme applied.'''
    return sg.Text(
        text,
        size=(width, 1),
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
        pad=(theme.T1_SIZE//3)*2,
        text_color=theme.TEXT_PRIMARY,
        background_color=theme.BG_PRIMARY,
    )


def create_stat_field(name: str, key: str) -> sg.Column:
    '''Create a stat field with his description and score.

    Args: 
        name : descriptive field.
        key : key on the summary of the score.
    Returns: 
        A column with the stat and the score obtained.'''
    width = FIELD_MAX_CHARACTERS - len(name)
    summary[key] = create_stat_type(' ', width)
    return sg.Column(
        [[create_stat_type(name), summary[key]]],
        background_color=theme.BG_PRIMARY
    )


def create_summary() -> sg.Column:
    '''Create the summary of the scores obtained for each field.

    Returns:
        Two columns with the information of the score obtained by the player.'''
    left_layout = [
        [create_stat_field('Puntos totales:', 'total_points')],
        [create_stat_field('Cantidad rondas:', 'total_rounds')],
        [create_stat_field('Rondas ganadas:', 'rounds_winned')],
        [create_stat_field('Rondas salteadas:', 'rounds_skiped')],
        [create_stat_field('Tiempo total (seg):', 'total_time')],
    ]
    right_layout = [
        [create_stat_field('Total intentos:', 'total_tryes')],
        [create_stat_field('Rondas completadas:', 'rounds_completed')],
        [create_stat_field('Rondas perdidas:', 'rounds_loosed')],
        [create_stat_field('Rondas sin tiempo:', 'rounds_timeout')],
        [create_stat_field('Tiempo promedio (seg):', 'average_time')],
    ]
    return sg.Column(
        [[
            sg.Column(left_layout, background_color=theme.BG_PRIMARY),
            _csg.horizontal_spacer(
                theme.scale(32), background_color=theme.BG_SECONDARY
            ),
            sg.Column(right_layout, background_color=theme.BG_PRIMARY),
        ]],
        background_color=theme.BG_SECONDARY,
    )


def refresh_summary(stats: dict[str, int]) -> None:
    '''Updates the content for the run summary.

    Args: 
        stats : stadistics generated at game screen.'''
    for key, value in stats.items():
        summary[key].update(str(value))


observer.subscribe(constants.RUN_RESULT, refresh_summary)


def create_nav_buttons() -> sg.Column:
    '''Generate the buttons to navigate to other screens.

    Returns: 
        A column with the navigation buttons correctly themed.'''
    padding = (theme.scale(16), theme.scale(16))
    buttons = [
        _common.navigation_button('Menu Principal', '-MENU-', padding=padding),
        _common.navigation_button('Volver a Jugar', '-GAME-', padding=padding),
        _common.navigation_button(
            'Nuevo Juego', '-CONFIGURE-GAME-', padding=padding
        ),
    ]
    return sg.Column(
        [buttons],
        background_color=theme.BG_BASE,
        element_justification='center'
    )


screen_layout = [
    [_common.screen_title('resultado', True)],
    [sg.VPush(theme.BG_BASE)],
    [create_summary()],
    [sg.VPush(theme.BG_BASE)],
    [create_nav_buttons()],
    [_csg.vertical_spacer(theme.scale(96), background_color=theme.BG_BASE)],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def screen_reset():
    '''Reset the screen content to a default/updated state.'''
    pass
