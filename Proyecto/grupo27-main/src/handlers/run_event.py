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
    START = 'inicio_partida' # nombre de los eventos
    TRY = 'intento'
    END = 'fin'


class EventStates(Enum): # Eventos de estados
    ERROR = 'error'
    OK = 'ok'
    TIME_OUT = 'timeout'
    ENDED = 'finalizada'
    CANCELED = 'cancelada'
    DEFAULT = ''


class RunEventRecorder:
    '''Registrador de los eventos ocurridos durante la ejecución del juego.'''

    def __init__(self, events_folder_path: str, users_ctr: UsersController, difficulty_ctr: DifficultyController) -> None:
        '''Inicialización del archivo utilizado para guardar la información de los eventos.

        Args:
           events_folder_path : Ruta del archivo que estaremos trabajando.
           user_ctr : Un controlador de usuario para acceder al usuario actual.
           difficulty_ctr : A difficulty controller to access to the current difficulty.'''
        self._file_path = os.path.join(events_folder_path, 'events.csv')
        self._users_ctr = users_ctr
        self._difficulty_ctr = difficulty_ctr
        self._uid = ''
        # El controlador se esta suscribiendo al evento "RUN_EVENT" y cuando cambia se ejecuta el metodo "record"
        observer.subscribe(constants.RUN_EVENT, self.record)

    def record(self, event_data: dict[str, Any]) -> None:
        '''Register an event on the event list.

        Args:
            event_data: datos del evento compuesto por
                nombre, N de rondas, usuario actual, estado, respuesta del usuario, respuesta correcta y dificultad'''
        if event_data['name'] == EventNames.START: # Si el nombre es el inicio significa que es una partida nueva
            self._uid = uuid.uuid4().hex
        event = [
            f'{time.time():.4f}',
            self._uid,
            self._users_ctr.user.nick, #desde el controlador el usuario actual
            self._users_ctr.user.gender,
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
