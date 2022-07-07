import csv
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
        self._users_ctr = users_ctr
        self._difficulty_ctr = difficulty_ctr
        self._uid = ''
        observer.subscribe(constants.RUN_EVENT, self.record)

    def record(self, event_data: dict[str, Any]) -> None:
        '''Register an event on the event list.

        Args:
            event_data: data of the event composed by 
                name,Q of rounds,current user,state,user answer, correct answer and difficulty'''
        if event_data['name'] == EventNames.START:
            self._uid = uuid.uuid4().hex
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
        self._save(event)

    def _default_header(self) -> list[str]:
        '''Return the header of the csv to use like default.'''
        return ['timestamp', 'id', 'usuarie', 'genero', 'nivel', 'cantidad a adivinar', 'evento', 'estado', 'correcta', 'respuesta']

    def _save(self, event: list[str]) -> None:
        '''Save the event at the end of the csv file.'''
        try:
            with open(self._file_path, mode='r+', encoding='utf-8', newline='') as csvfile:
                csvfile.seek(0, 2)
                writer = csv.writer(csvfile)
                writer.writerow(event)
        except FileNotFoundError:
            events: list[list[str]] = [self._default_header(), event]
            file.save_csv(self._file_path, events)
