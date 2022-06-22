from typing import Any, Callable, TypedDict

from .. import constants, default
from . import observer, difficulty, file


DEFAULT_PREFERRED_COLOR = '#000000'
DEFAULT_PREFERRED_DIFFICULTY = difficulty.DEFAULT_TYPE


class UserJSON(TypedDict):
    nick: str
    age: int
    gender: str
    preferred_color: str
    preferred_difficulty: str
    custom_difficulty: dict[str, int]
    scores: dict[str, list[int]]


def default_scores() -> dict[str, list[int]]:
    return {
        'easy': [],
        'normal': [],
        'hard': [],
        'insane': [],
        'custom': []
    }


class User:
    def __init__(self, definition: UserJSON) -> None:
        self._nick = definition['nick']
        self._age = definition['age']
        self._gender = definition['gender']
        self._preferred_color = definition['preferred_color']
        self._preferred_difficulty = definition.get(
            'preferred_difficulty', DEFAULT_PREFERRED_DIFFICULTY
        )
        self._custom_difficulty = difficulty.Difficulty(
            **definition.get('custom_difficulty', default.DIFFICULTIES['custom'])
        )
        self._scores = definition.get('scores', default_scores())

    @property
    def nick(self) -> str:
        return self._nick

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    @property
    def preferred_color(self) -> str:
        return self._preferred_color

    @property
    def preferred_difficulty(self) -> str:
        return self._preferred_difficulty

    @preferred_difficulty.setter
    def preferred_difficulty(self, type: str) -> None:
        self._preferred_difficulty = type

    @property
    def custom_difficulty(self) -> difficulty.Difficulty:
        return self._custom_difficulty

    @property
    def scores(self) -> dict[str, list[int]]:
        return self._scores

    @property
    def sorted_scores(self) -> dict[str, list[int]]:
        return {
            difficulty: sorted(results) for difficulty, results in self._scores.items()
        }

    def update_score(self, difficulty: str, value: int) -> None:
        self._scores[difficulty].append(value)

    def get_score(self, difficulty: str) -> list[int]:
        return self._scores[difficulty]

    def jsonify(self) -> UserJSON:
        return {
            'nick': self._nick,
            'age': self._age,
            'gender': self._gender,
            'preferred_color': self._preferred_color,
            'preferred_difficulty': self._preferred_difficulty,
            'custom_difficulty': self._custom_difficulty.jsonify(),
            'scores': self._scores
        }


def new_user(nick: str, age: int, gender: str, preferred_color: str = DEFAULT_PREFERRED_COLOR) -> User:
    return User({
        'nick': nick,
        'age': age,
        'gender': gender,
        'preferred_color': preferred_color,
        'preferred_difficulty': DEFAULT_PREFERRED_DIFFICULTY,
        'custom_difficulty': default.DIFFICULTIES['custom'],
        'scores': default_scores()
    })


class UsersController:
    def __init__(self, users_path: str, default_user: str = '') -> None:
        self._file_path = users_path
        raw_users: dict[str, UserJSON] = file.load_json(users_path, dict())
        self._users = {
            nick: User(definition) for nick, definition in raw_users.items()
        }
        self._current_user: str = default_user
        observer.subscribe(
            difficulty.UPDATE_DIFFICULTY_TYPE, self._set_user_difficulty
        )

    def add(self, nick: str, age: int, gender: str, preferred_color: str = '#000000') -> None:
        self._users[nick] = new_user(nick, age, gender, preferred_color)

    def remove(self, nick: str) -> None:
        if self._current_user == nick:
            self.current_user = 'undefined'
        self._users.pop(nick, None)

    @property
    def user_list(self) -> list[User]:
        return [user for _, user in self._users.items()]

    def users_transform(self, fn: Callable[[User], Any]) -> list[Any]:
        return [fn(user) for _, user in self._users.items()]

    def user(self, nick: str) -> User:
        return self._users[nick]

    def user_transform(self, nick: str, fn: Callable[[User], Any]) -> User:
        return fn(self._users[nick])

    @property
    def current_user(self) -> User:
        return self._users.get(
            self._current_user, new_user('undefined', 0, 'undefined')
        )

    @current_user.setter
    def current_user(self, nick: str) -> None:
        self._current_user = nick
        observer.post_event(constants.USER_CHANGE, self.current_user)

    def _set_user_difficulty(self, type: str) -> None:
        self.current_user.preferred_difficulty = type 

    def save(self) -> None:
        file.save_json(
            self._file_path,
            {nick: user.jsonify() for nick, user in self._users.items()},
        )
