import os
import time
import uuid
from enum import Enum
from typing import Any

from .. import constants, translations
from . import file, observer
from .user import UsersController
from .difficulty import DifficultyController


class EventNames(Enum):
    START = 'inicio_partida'
    TRY = 'intento'
    END = 'fin'


class EventStates(Enum):
    ERROR = 'error'
    OK = 'ok'
    TIME_OUT = 'timeout'
    ENDED = 'finalizada'
    CANCELED = 'cancelada'
    DEFAULT = ''


class RunEventRecorder:
    '''Recorder of the events occurred during the execution of the game.'''
    def __init__(self, events_folder_path: str, users_ctr: UsersController, difficulty_ctr: DifficultyController) -> None:
        '''Initialization of the file used for save the information of the events.

        Args:
           events_folder_path : Path of the file that we will be working.
           user_ctr : A user controller to access to the current user.
           difficulty_ctr : A difficulty controller to access to the current difficulty.'''
        self._file_path = os.path.join(events_folder_path, 'events.csv')

        self._events = file.load_csv(
            self._file_path, [self._default_header()]
        )
        self._users_ctr = users_ctr
        self._difficulty_ctr = difficulty_ctr
        self._uid = ''
        self._playing = False
        observer.subscribe(constants.RUN_EVENT, self.record)

    def record(self, event_data: dict[str, Any]) -> None:
        '''Register an event on the event list.

        Args:
            event_data: data of the event composed by 
                name,Q of rounds,current user,state,user answer, correct answer and difficulty'''
        if event_data['name'] == EventNames.START:
            self._uid = uuid.uuid4().hex
            self._playing = True
        elif event_data['name'] == EventNames.END:
            self._playing = False
        event = [
            f'{time.time():.4f}',
            self._uid,
            self._users_ctr.current_user.nick,
            self._users_ctr.current_user.gender,
            translations.DIFFICULTY_TO_ES[self._difficulty_ctr.difficulty_name],
            event_data['rounds'],
            event_data['name'].value,
            event_data.get('state', EventStates.DEFAULT).value,
            event_data.get('correct_answer', EventStates.DEFAULT.value),
            event_data.get('user_answer', EventStates.DEFAULT.value),
        ]
        self._events.append(event)

    def _default_header(self) -> list[str]:
        '''Return the header of the csv to use like default.'''
        return ['timestamp', 'id', 'usuarie', 'genero', 'nivel', 'cantidad a adivinar', 'evento', 'estado', 'correcta', 'respuesta']

    def save(self) -> None:
        '''Save the list of events into a csv file.

        Before saving checks if the player was playing to do the END event.'''
        if self._playing:
            event_data = {
                'name': EventNames.END,
                'rounds': self._difficulty_ctr.difficulty.rounds_per_game,
                'state': EventStates.CANCELED
            }
            self.record(event_data)
        file.save_csv(self._file_path, self._events)
