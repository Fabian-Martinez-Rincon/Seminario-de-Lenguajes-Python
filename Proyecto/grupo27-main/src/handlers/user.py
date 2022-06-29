from typing import Any, Callable, TypedDict

from .. import constants, default
from . import observer, difficulty, file


class UserJSON(TypedDict):
    '''Dict version of a user.'''
    nick: str
    age: int
    gender: str
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
    '''Class that models an application user.'''

    def __init__(self, definition: UserJSON) -> None:
        '''Initializes the user object.

        Args:
            definition: a dict containing user related values.'''
        self._nick = definition['nick']
        self._age = definition['age']
        self._gender = definition['gender']
        self._preferred_difficulty = definition['preferred_difficulty']
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
        '''A dict containing user's scores for each difficulty.'''
        return self._scores

    @property
    def sorted_scores(self) -> dict[str, list[int]]:
        '''A dict containing user's sorted scores for each difficulty.'''
        return {
            difficulty: sorted(results) for difficulty, results in self._scores.items()
        }

    def update_score(self, difficulty: str, value: int) -> None:
        '''Adds a new score to the specified difficulty.

        Args:
            difficulty: the difficulty name in which the score will be added.
            value: the score itself.'''
        self._scores[difficulty].append(value)

    def get_score(self, difficulty: str) -> list[int]:
        '''Returns all scores for the specified difficulty.

        Args:
            difficulty: the difficulty of the scores.
        Returns
            all scores.'''
        return self._scores[difficulty]

    def jsonify(self) -> UserJSON:
        '''Generates a dict representation of every attribute.

        Returns:
            the generated dictionary.'''
        return {
            'nick': self._nick,
            'age': self._age,
            'gender': self._gender,
            'preferred_difficulty': self._preferred_difficulty,
            'custom_difficulty': self._custom_difficulty.jsonify(),
            'scores': self._scores
        }


def new_user(nick: str, age: int, gender: str) -> User:
    '''Creates a new User instance with predefined initializations.'''
    return User({
        'nick': nick,
        'age': age,
        'gender': gender,
        'preferred_difficulty': default.DIFFICULTY_NAME,
        'custom_difficulty': default.DIFFICULTIES['custom'],
        'scores': default_scores()
    })


class UsersController:
    '''Class for controlling application users.'''

    def __init__(self, users_path: str, default_user: str = '') -> None:
        '''Loads the saved users if there are.

        Args:
            settings_path: absolute json file path of saved users.
            default_user: the nick for the starting user.'''
        self._file_path = users_path
        raw_users: dict[str, UserJSON] = file.load_json(users_path, dict())
        self._users = {
            nick: User(definition) for nick, definition in raw_users.items()
        }
        self._current_user: str = default_user
        observer.subscribe(
            constants.UPDATE_DIFFICULTY_TYPE, self._set_user_difficulty
        )

    def add(self, nick: str, age: int, gender: str) -> None:
        '''Creates a new user.'''
        self._users[nick] = new_user(nick, age, gender)

    def remove(self, nick: str) -> None:
        '''Removes the specified user and its saved state.

        Args:
            nick: the nick of the user to be removed.'''
        if self._current_user == nick:
            self._current_user = 'undefined'
        self._users.pop(nick, None)

    @property
    def user(self) -> User:
        return self._users.get(
            self._current_user, new_user('undefined', 0, 'undefined')
        )

    @user.setter
    def user(self, nick: str) -> None:
        self._current_user = nick
        observer.post_event(constants.USER_CHANGE, self.user)

    def get_user(self, nick: str) -> User:
        '''Returns a user by the specified nick (must be valid).'''
        return self._users[nick]

    @property
    def user_list(self) -> list[User]:
        '''A list of all registered users.'''
        return [user for _, user in self._users.items()]

    def transform_user(self, nick: str, fn: Callable[[User], Any]) -> Any:
        '''Returns the result of applying a fn to the specified user by nick.'''
        return fn(self._users[nick])

    def transform_users(self, fn: Callable[[User], Any]) -> list[Any]:
        '''A map implementation for users.

        Args:
            fn: a function that receives a user and return something.
        Returns:
            a list with the result of the function applied for every user.'''
        return [fn(user) for _, user in self._users.items()]

    def _set_user_difficulty(self, name: str) -> None:
        self.user.preferred_difficulty = name

    def save(self) -> None:
        '''Saves the users states into its json file path.'''
        file.save_json(
            self._file_path,
            {nick: user.jsonify() for nick, user in self._users.items()},
        )
