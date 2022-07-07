from dataclasses import dataclass
from random import randint

from . import file


class Dataset:
    '''Clase que modela un dataset.'''

    def __init__(self, name: str, raw_dataset: list[list[str]]) -> None:
        '''Inicializa el objeto del dataset.

        Args:
            name: the name that identifies the dataset.
            raw_dataset: the dataset definition.'''
        self._name = name
        self._header = raw_dataset[0]
        self._content = raw_dataset[1:]
        self._used: set[int] = set() # pregunta

    @property
    def name(self) -> str:
        return self._name

    @property
    def header(self) -> list[str]:
        return self._header

    def _random(self) -> list[str]:
        sample = randint(0, len(self._content) - 1)
        return self._content[sample]

    def _random_unique(self) -> list[str]:
        while True:
            sample = randint(0, len(self._content) - 1)
            if sample not in self._used:
                self._used.add(sample)
                break
        return self._content[sample]

    def random_sample(self, size: int, unique: int = 0) -> list[list[str]]:
        '''Genera una muestra del contenido del dataset.

        Args:
            size: the number of samples.
            unique: el número de muestras que no se muestrearon previamente en términos de otras muestras únicas.    
        Returns:
            la lista de muestras, las muestras únicas son las primeras en la lista'''
        samples: list[list[str]] = []
        for _ in range(size):
            if unique > 0:
                samples.append(self._random_unique())
                unique -= 1
            else:
                sample = self._random()
                while sample in samples:
                    sample = self._random()
                samples.append(sample)
        return samples

    def reset(self) -> None:
        '''Resets the used samples record.'''
        self._used = set()


@dataclass
class Card:
    '''Class that contains card information.'''
    hints: list[str]
    correct_answer: str
    bad_anwers: list[str]


class CardController:
    '''Class for controlling logic related to cards.'''

    def __init__(self, datasets_folder_path: str) -> None:
        '''Stores the path to the datasets and scans it.

        Args:
            datasets_folder_path: absolute directory path of datasets.'''
        self._folder_path = datasets_folder_path
        self._find_datasets()
        if self.no_datasets:
            self._load_generic_dataset()
        else:
            name = list(self._datasets.keys())[0]
            self._load_dataset(name)

    def _find_datasets(self) -> None:
        file.ensure_dirs(self._folder_path)
        self._datasets = {
            file_name.split('.')[0]: path 
            for file_name, path in file.scan_dir(self._folder_path, file_extension='.csv')
        }

    @property
    def no_datasets(self) -> bool:
        return len(self._datasets) == 0

    def _load_generic_dataset(self) -> None:
        self._dataset = Dataset(
            'Error at loading dataset',
            [
                [f'empty-{n_rows}-{n_columns}' for n_columns in range(6)]
                for n_rows in range(64)
            ]
        )

    def _load_dataset(self, name: str) -> None:
        raw_dataset = file.load_csv(self._datasets[name], [], read_only=True)
        if raw_dataset == []:
            self._load_generic_dataset()
        else:
            self._dataset = Dataset(name, raw_dataset)

    def reset(self) -> None:
        '''Resets the current dataset state.'''
        self._dataset.reset()

    @property
    def types_list(self) -> list[str]:
        '''Updated list of available datasets.'''
        self._find_datasets()
        return [key for key in self._datasets]

    @property
    def type(self) -> str:
        '''The current dataset type.'''
        return self._dataset.name

    @type.setter
    def type(self, type: str) -> None:
        self._load_dataset(type)

    @property
    def characteristics(self) -> list[str]:
        '''List of meanings for the card hints and answers.'''
        return self._dataset.header

    @property
    def new_card(self) -> Card:
        correct, *bads = self._dataset.random_sample(5, unique=1)
        return Card(
            correct[:-1], correct[-1], [bad[-1] for bad in bads]
        )
