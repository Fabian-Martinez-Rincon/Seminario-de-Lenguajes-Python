'''Wrappers of sg elements.

Collection of wrapper classes/functions around sg elements to add facility at GUI development.'''
from abc import ABC, abstractmethod
from typing import Any

import PySimpleGUI as sg

from .. import constants


Element = Any
LayoutRow = list[Element]
CompleteLayout = list[LayoutRow]


class ChainedElement(ABC):
    '''Abstract Base Class to implement a method chaining behaviour for creating a sg layout.'''
    @abstractmethod
    def __init__(self, **column_parameters: Any) -> None:
        ...

    @abstractmethod
    def add(self, content: Element | LayoutRow | CompleteLayout) -> Any:
        ...

    @abstractmethod
    def pack(self) -> sg.Column:
        ...


class HorizontalList(ChainedElement):
    '''Class to create a layout like a horizontal list capable of method chaining.'''

    def __init__(self, **column_parameters: Any) -> None:
        '''Initializes the attributes of the columns that works as containers.

        Args:
            column_parameters: kargs that a normal sg.Column would accept.'''
        self._container: list[Element] = []
        self._config = column_parameters

    def add(self, content: Element | LayoutRow | CompleteLayout) -> 'HorizontalList':
        '''Add to the list matching if is a element of a layout.

        Args: 
            content: the content to add to the list.
        Returns: 
            the current information of the class after add the element pass by argument.'''
        match content:
            case [[*_], *_]:
                element = sg.Column(content, **self._config)
            case [*_]:
                element = sg.Column([content], **self._config)
            case _:
                element = content
        self._container.append(element)
        return self

    def pack(self) -> sg.Column:
        '''Packs the list item into a column.'''
        return sg.Column([self._container], **self._config)


class VerticalList(ChainedElement):
    '''Class to create a layout like a vertical list capable of method chaining.'''

    def __init__(self, **column_parameters: Any) -> None:
        '''Initializes the attributes of the columns that works as containers.

        Args:
            column_parameters: kargs that a normal sg.Column would accept.'''
        self._container: CompleteLayout = []
        self._config = column_parameters

    def add(self, content: Element | LayoutRow | CompleteLayout) -> 'VerticalList':
        '''Add to the list matching if is a element of a layout.

        Args: 
            content: content to add to the list.
        Returns: 
            the current information of the class after add the element pass by argument.'''
        match content:
            case [[*_], *_]:
                element = [sg.Column(content, **self._config)]
            case [*_]:
                element = content
            case _:
                element = [content]
        self._container.append(element)
        return self

    def pack(self) -> sg.Column:
        'Packs the list item into a column.'
        return sg.Column(self._container, **self._config)


def centered(content: Element | LayoutRow | CompleteLayout, horizontal_only: bool = False, **column_parameters: Any) -> sg.Column:
    '''Centers a content into a column.

    Args:
        content: content to be centered.
        horizontal_only: default : false.
        column_parameters: all the column parameter that will be applied as a configuration.
    Returns: 
        A column with the content centered and column parameters applied.'''
    column_parameters['element_justification'] = 'center'
    column_parameters['expand_y'] = not horizontal_only
    column_parameters['expand_x'] = True
    column_parameters['pad'] = 0
    background_color = column_parameters.get('background_color', None)

    match content:
        case [[sg.Element(), *_], *_]:
            layout = content
        case [sg.Element(), *_]:
            layout = [content]
        case sg.Element():
            layout = [[content]]
        case _:
            raise ValueError(
                f'content must be a Element | LayoutRow | CompleteLayout, content={content} not correct'
            )
    layout = layout if horizontal_only else [
        [sg.VPush(background_color)], *layout, [sg.VPush(background_color)]
    ]
    return sg.Column(
        layout,
        **column_parameters
    )


def horizontal_spacer(width: int, background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=(width, 0), background_color=background_color)


def vertical_spacer(height: int, background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=(0, height), background_color=background_color)


def custom_popup(layout: CompleteLayout, background_color: str | None = None, duration: int | None = None) -> str:
    '''Generates a custom pop up window.

    The pop-up closes on any event produced returning the key of the event or constants.EXIT_APPLICATION in other case.

    Args:
        layout: layout that will display the popup.
        background_color: default : None.
        duration: duration in seconds to close the pop up. default: none(permanently until close it).
    Returns: 
        A pop up with the theme applied and a timer for close it if is specified.'''
    window = sg.Window(
        'pop-up', layout, background_color=background_color,
        no_titlebar=True, keep_on_top=True, finalize=True,
        margins=(0, 0), resizable=False, modal=True,
        use_default_focus=False
    )

    timeout = duration * 1000 if duration else None
    try:
        while True:
            event, _ = window.read(timeout=timeout, timeout_key='-TIME-OUT-')
            if event is None or event == '-TIME-OUT-':
                event = constants.EXIT_APPLICATION
                break
            event = event.rstrip('0123456789')
            break
    finally:
        window.close()
    return event
