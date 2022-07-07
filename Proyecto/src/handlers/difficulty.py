from copy import copy
# Las declaraciones de asignación en Python no copian objetos, crean enlaces entre un objetivo y un objeto. A veces se necesita una copia para poder cambiar una copia sin cambiar la otra.
from dataclasses import dataclass
from typing import Any
# Tipo especial que indica un tipo sin restricciones.
# Todos los tipos son compatibles con Any.
# Any es compatible con todos los tipos

from .. import constants, default # tiene las rutas de los archivos  y default tiene las configuraciones generales del juego, dificultades y colores del juego
from . import observer, file # El observer 


DEFAULT_TYPE = 'normal'

#Este módulo proporciona un decorador y funciones para agregar automáticamente métodos especiales generados como __init__() a clases definidas por el usuario.
# El decorador devuelve la misma clase, no crea ninguna nueva

# Fuente: https://peps.python.org/pep-0557/
# Solo representa datos
@dataclass
class Difficulty:
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    characteristics_shown: int

    # Cambio los datos dependiendo de la dificultad elegida por el usuario
    def swap(self, new: 'Difficulty') -> None: # swap/intercambio
        self.time_per_round = new.time_per_round # new es solo el nombre
        self.rounds_per_game = new.rounds_per_game
        self.points_correct_answer = new.points_correct_answer
        self.points_bad_answer = new.points_bad_answer
        self.characteristics_shown = new.characteristics_shown

    # Retorna un diccionario con todos los datos de la partida
    def jsonify(self) -> dict[str, int]:
        return {
            'time_per_round': self.time_per_round,
            'rounds_per_game': self.rounds_per_game,
            'points_correct_answer': self.points_correct_answer,
            'points_bad_answer': self.points_bad_answer,
            'characteristics_shown': self.characteristics_shown
        }

# Cargo las dificultades de json
class DifficultyController:
    def __init__(self, difficulties_path: str, difficulty: str = DEFAULT_TYPE) -> None:
        self._file_path = difficulties_path
        self._current_difficulty = difficulty # actual
        raw_difficulties: dict[str, dict[str, int]] = file.load_json( # Cargamos el json con las configuraciones de dificultad
            difficulties_path, default.DIFFICULTIES
        )
        self._difficulties = {# ** la composicion del diccionario (clave,valor(desenpaquetamos el diccionario))
            name: Difficulty(**definition) for name, definition in raw_difficulties.items()
        }
        self._difficulty = copy(self._difficulties[self._current_difficulty]) # Me quedo con una copia de la dificultad actual
        # Observer es un patrón de diseño de comportamiento que permite a un objeto notificar a otros objetos sobre cambios en su estado
        # Proporciona una forma de reaccionar a los eventos que suceden en otros objetos, sin acoplarse a sus clases.

        # El controlador se esta suscribiendo al evento "USER_CHANGE" y cuando cambia se ejecuta el metodo "_new_user"
        observer.subscribe(constants.USER_CHANGE, self._new_user)

    @property
    def difficulty(self) -> Difficulty:
        return self._difficulty

    @property
    def difficulty_name(self) -> str:
        return self._current_difficulty

    def update_difficulty( # update = actualizacion para identificar cuando cambiamos los valores
        self, time_per_round: int | None = None,
        rounds_per_game: int | None = None, points_correct_answer: int | None = None,
        points_bad_answer: int | None = None, characteristics_shown: int | None = None,
    ) -> None:
        if time_per_round: # not is none
            self._difficulties['custom'].time_per_round = time_per_round
        # La equivalente
        # if time_per_round not is none: 
        #    self._difficulties['custom'].time_per_round = time_per_round
        if rounds_per_game:
            self._difficulties['custom'].rounds_per_game = rounds_per_game
        if points_correct_answer is not None:
            self._difficulties['custom'].points_correct_answer = points_correct_answer
        if points_bad_answer is not None:
            if points_bad_answer > 0:
                points_bad_answer *= -1
            self._difficulties['custom'].points_bad_answer = points_bad_answer
        if characteristics_shown is not None:
            self._difficulties['custom'].characteristics_shown = characteristics_shown
        self.set_difficulty('custom')

    def set_difficulty(self, type: str) -> None:
        self._current_difficulty = type 
        self._difficulty.swap(self._difficulties[type])
        # Publico un envento y cambio la dificultad
        # notifica a posibles suscriptores y la data asociada
        observer.post_event(constants.UPDATE_DIFFICULTY_TYPE, type) # type informacion asociada al evento
        
    # Retorno un diccionario con el nombre de la dificultad
    # y un objeto que contiene los datos asociados a la dificultad
    def difficulties(self) -> dict[str, Difficulty]: 
        return {name: copy(definition) for name, definition in self._difficulties.items()}

    # Se modifica solo la dificultad custom ya que las otras dificultades no se tienen que tocar
    def _new_user(self, user: Any) -> None:
        self._difficulties['custom'] = user.custom_difficulty
        self.set_difficulty(user.preferred_difficulty)

    def save(self) -> None:
        file.save_json(
            self._file_path,
            self._difficulties,
            is_custom_class=True
        )
