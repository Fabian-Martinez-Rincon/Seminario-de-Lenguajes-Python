'''Rankings of best scores for all difficulties.'''
from typing import Any

import PySimpleGUI as sg

from .. import translations
from ..controllers import theme, users_controller as users_ctr
from . import _common, _csg


SCREEN_NAME = '-RANKING-'
HISTORIAL_SIZE = 20


rankings_runs: dict[str, sg.Multiline] = {
    'easy': Any,
    'normal': Any,
    'hard': Any,
    'insane': Any,
    'custom': Any
}
rankings_averages: dict[str, sg.Multiline] = {
    'easy': Any,
    'normal': Any,
    'hard': Any,
    'insane': Any,
    'custom': Any
}

NameScores = tuple[str, dict[str, list[int]]]


def get_name_and_scores(user: Any) -> NameScores:
    '''Return the name and score of an User.

    Args:
        user : the user to get the name and score.
    Returns:
        A tuple with the nick and scores.'''
    return user.nick, user.sorted_scores


def rank_header(name: str) -> sg.Text:
    '''Header of a column.

    Args:
        name: name of the header needed.
    Returns:
        A sg.Text with the theme applied and the text passed by argument.'''
    return sg.Text(
        translations.DIFFICULTY_TO_ES[name],
        size=(16, 1),
        background_color=theme.BG_PRIMARY,
        text_color=theme.TEXT_ACCENT,
        font=(theme.FONT_FAMILY_TEXT, theme.T1_SIZE),
        justification='center',
    )


def rank_content(scores: list[tuple[int, str]]) -> str:
    '''Content of the ranking table.

    Manipulate the information to display it correctly on the screen. Sort the first 20 scores.

    Args:
        scores: scores that need to be ordered before display it.
    Returns:
        A string of the 20 first scores line per line.'''
    content: list[str] = []
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    for i in range(HISTORIAL_SIZE):
        if i < len(scores):
            score, name = scores[i]
            row = f' {i+1:>2}{score:>6}{name:^15} '
        else:
            row = '\n'
        content.append(row)
    return '\n'.join(content)


def create_rank(scores: str) -> sg.Multiline:
    '''Create the content of a column.

    Args:
        scores: the string with the scores to display.
    Returns: 
        A multiline text with all the info of the scores with the theme applied correctly for the layout.'''
    return sg.Multiline(
        scores,
        size=(1, 20),
        disabled=True,
        font=(theme.FONT_FAMILY_TEXT, theme.T2_SIZE),
        justification='center',
        no_scrollbar=True,
        text_color=theme.TEXT_ACCENT,
        background_color=theme.BG_PRIMARY,
        expand_x=True,
        border_width=0
    )


def create_runs_rank() -> sg.Column:
    '''Create a global ranking of runs scores for each difficulty.'''
    ranks = _csg.HorizontalList(pad=(0, 0), background_color=theme.BG_SECONDARY)
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings_runs:
        all_scores = [
            (score, nick) for nick, scores in users for score in scores[difficulty]
        ]
        rankings_runs[difficulty] = create_rank(rank_content(all_scores))
        ranks.add([
            [rank_header(difficulty)],
            [rankings_runs[difficulty]]
        ])
    return ranks.pack()


def create_averages_rank() -> sg.Column:
    '''Create a global ranking of average runs scores by user for each difficulty.'''
    ranks = _csg.HorizontalList(pad=(0, 0), background_color=theme.BG_SECONDARY)
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings_averages:
        all_scores = [
            (sum(scores[difficulty])//len(scores[difficulty]), nick) for nick, scores in users if len(scores[difficulty]) > 0
        ]
        rankings_averages[difficulty] = create_rank(rank_content(all_scores))
        ranks.add([
            [rank_header(difficulty)],
            [rankings_averages[difficulty]]
        ])
    return ranks.pack()


def create_ranking() -> sg.TabGroup:
    '''Create a TabGroup where each tab is a ranking.'''
    return sg.TabGroup(
        [
            [sg.Tab('Partidas', [[create_runs_rank()]], pad=0)],
            [sg.Tab('Promedios', [[create_averages_rank()]], pad=0)]
        ],
        tab_location='top',
        title_color=theme.TEXT_SECONDARY,
        tab_background_color=theme.BG_PRIMARY,
        selected_title_color=theme.TEXT_ACCENT,
        selected_background_color=theme.BG_SECONDARY,
        background_color=theme.BG_BASE,
        focus_color=theme.BG_SECONDARY,
        font=(theme.FONT_FAMILY, theme.H4_SIZE),
        pad=0,
        border_width=0,
        tab_border_width=1,
        expand_x=False,
        expand_y=False,
    )


def refresh_ranking() -> None:
    '''Refresh all the rankings with the latest information.'''
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings_runs:
        all_scores = [
            (score, nick) for nick, scores in users for score in scores[difficulty]
        ]
        rankings_runs[difficulty].update(rank_content(all_scores))

    for difficulty in rankings_averages:
        all_scores = [
            (sum(scores[difficulty])//len(scores[difficulty]), nick) for nick, scores in users if len(scores[difficulty]) > 0
        ] 
        rankings_averages[difficulty].update(rank_content(all_scores))


screen_layout = [
    [_common.screen_title('ranking', True)],
    [sg.VPush(theme.BG_BASE)],
    [create_ranking()],
    [sg.VPush(theme.BG_BASE)],
    [_common.navigation_button('Menu Principal', '-MENU-', padding=(theme.scale(64),)*2),
     sg.Push(theme.BG_BASE)],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def screen_reset() -> None:
    '''Reset the screen content to a default/updated state.'''
    refresh_ranking()
