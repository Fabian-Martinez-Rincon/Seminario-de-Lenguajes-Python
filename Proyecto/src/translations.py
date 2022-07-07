'''Contains dictionaries used for translation from logic to GUI and vice versa.'''


class TranslationDict:
    '''Acts like a dict object but instead of raising a KeyError if key not present, returns the key as value.'''

    def __init__(self, translation_dict: dict[str, str]) -> None:
        '''Initializes the inner translation dictionary.

        Args:
            translation_dict: a dict in which key is the world/frase to be translated and value is the translation.'''
        self._dict = translation_dict

    def __getitem__(self, key: str) -> str:
        '''Method called when using [].'''
        if key not in self._dict:
            return key
        return self._dict[key]

    def __call__(self, key: str) -> str:
        '''Method called when using ().'''
        if key not in self._dict:
            return key
        return self._dict[key]

    def __contains__(self, key: str) -> bool:
        '''Method called at operation 'in'.'''
        return key in self._dict

    def __str__(self) -> str:
        '''Method called to get the string representation.'''
        return 'Translations = ' + ', '.join([f'{key} : {value}' for key, value in self._dict.items()])


DIFFICULTY_TO_ES = {
    'easy': 'Fácil',
    'normal': 'Intermedio',
    'hard': 'Difícil',
    'insane': 'Insano',
    'custom': 'Personalizada',
}
DIFFICULTY_TO_EN = {
    'Fácil': 'easy',
    'Intermedio': 'normal',
    'Difícil': 'hard',
    'Insano': 'insane',
    'Personalizada': 'custom',
}
DATASET_HEADER = {
    'spotify': ['Top genero', 'Tipo artista', 'Año lanzamiento', 'Mejor año', 'BPM', 'Artista'],
    'fifa': ['Equipo', 'Nacionalidad', 'Posición', 'Edad', 'Potencial', 'Nombre'],
}
DATASET_TO_ES = TranslationDict({
    'fifa': 'FIFA 21',
    'spotify': 'Spotify',
    'lakes': 'Lagos Argentina'
})
DATASET_TO_EN = TranslationDict({
    'FIFA 21': 'fifa',
    'Spotify': 'spotify',
    'Lagos Argentina': 'lakes'
})
