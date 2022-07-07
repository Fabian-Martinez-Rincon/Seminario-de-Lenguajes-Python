from dataclasses import dataclass
from random import randint

from . import file


class Dataset:  # Nombre y todos los datos del dataset
    def __init__(self, name: str, raw_dataset: list[list[str]]) -> None:
        self._name = name
        self._header = raw_dataset[0]
        self._content = raw_dataset[1:]
        # Genera un objeto iterable (para cualquier tipo de dato) si es un string lo genera random y en si son nros los genera ordenados
        self._used: set[int] = set()

    # Es un decorador que viene por defecto con Python, y puede ser usado para modificar un método para que sea un atributo o propiedad.

    @property
    def name(self) -> str:
        return self._name

    @property
    def header(self) -> list[str]:
        return self._header

    # Genera una fila random
    def _random(self) -> list[str]:
        sample = randint(0, len(self._content) - 1)
        return self._content[sample]

    # Retorna una fila random asegurando de que no se uso
    # Paso a used el indice de la fila utilizada y me salgo utilizando el breack
    def _random_unique(self) -> list[str]:
        while True:
            sample = randint(0, len(self._content) - 1)
            if sample not in self._used:
                self._used.add(sample)
                break
        return self._content[sample]

    # unique: cantidad de filas unicas
    def random_sample(self, size: int, unique: int = 0) -> list[list[str]]:
        samples: list[list[str]] = []
        # _ en python es descartado (convecion), a nosotros solo nos importa iterar el tamaño
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
        self._used = set()

#Este módulo proporciona un decorador y funciones para agregar automáticamente métodos especiales generados como __init__() a clases definidas por el usuario.
# El decorador devuelve la misma clase, no crea ninguna nueva

# Fuente: https://peps.python.org/pep-0557/
# Solo representa datos
@dataclass
class Card: # pista 
    hints: list[str]
    correct_answer: str
    bad_anwers: list[str]



class CardController:
    def __init__(self, datasets_folder_path: str) -> None:
        self._folder_path = datasets_folder_path #
        self._find_datasets()  # encontrar dataset (con la lista y los nombres)
        if self.no_datasets:
            self._load_generic_dataset() # Invoco el metodo porque no hay datasets y me quedo con el general
        else:
            name = list(self._datasets.keys())[0]# si hay datasets, me quedo con el primero
            self._load_dataset(name)

    def _find_datasets(self) -> None: # find encontrar
        file.ensure_dirs(self._folder_path) # se asegura de que la carpeta exista
        self._datasets = {                  # el _folder_path esta como atributo
            file_name.split('.')[0]: path   # Separamos el archivo de la extension  (generando una lista con sus respectivos nombres)
            for file_name, path in file.scan_dir(self._folder_path, file_extension='.csv')
        }

    @property
    def no_datasets(self) -> bool: # Retorna verdadero si no tengo datos en mi dataset
        return len(self._datasets) == 0

    def _load_generic_dataset(self) -> None: # el metodo genera un dataset con solo nros y de nombre 'Error at loading dataset'
        self._dataset = Dataset(             
            'Error at loading dataset',
            [
                [f'empty-{n_rows}-{n_columns}' for n_columns in range(6)]
                for n_rows in range(64)
            ]
        )

    def _load_dataset(self, name: str) -> None: # Cargo el datases con el nombre y los datos
        raw_dataset = file.load_csv(self._datasets[name], [], read_only=True)
        if raw_dataset == []:
            self._load_generic_dataset()
        else:
            self._dataset = Dataset(name, raw_dataset)

    def reset(self) -> None:
        self._dataset.reset()

    @property
    def types_list(self) -> list[str]:
        self._find_datasets()
        return [key for key in self._datasets]

    @property
    def type(self) -> str:
        return self._dataset.name

    @type.setter
    def type(self, type: str) -> None:
        self._load_dataset(type)

    @property
    def characteristics(self) -> list[str]:
        return self._dataset.header

    @property # hint = pista
    def new_card(self) -> Card: # Retorna la pregunta correcta y todas las incorrectas
        correct, *bads = self._dataset.random_sample(5, unique=1)
        return Card(
            correct[:-1], correct[-1], [bad[-1] for bad in bads] # pregunta
        )
