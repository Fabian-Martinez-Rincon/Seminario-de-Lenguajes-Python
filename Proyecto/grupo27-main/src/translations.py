'''Contiene diccionarios utilizados para la traducción de la lógica a la GUI y viceversa..'''


class TranslationDict:
    ''' Actúa como un objeto dict pero en lugar de generar un KeyError si la clave no está presente, devuelve la clave como valor.'''

    def __init__(self, translation_dict: dict[str, str]) -> None:
        '''Inicializa el diccionario con traducción.

        Argumentos:
            translation_dict: un dictado en el que la clave es el mundo/frase a traducir y el valor es la traducción.'''
        self._dict = translation_dict

    def __getitem__(self, key: str) -> str:
        '''Método llamado cuando se usa [].'''
        if key not in self._dict:
            return key
        return self._dict[key]

    def __call__(self, key: str) -> str:
        '''Método llamado cuando se usa ().'''
        if key not in self._dict:
            return key
        return self._dict[key]

    def __contains__(self, key: str) -> bool:
        '''Método llamado en la operación 'in'.'''
        return key in self._dict

    def __str__(self) -> str:
        '''Método llamado para obtener la representación del string.'''
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
