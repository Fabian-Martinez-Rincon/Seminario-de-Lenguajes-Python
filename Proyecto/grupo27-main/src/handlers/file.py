'''Contiene funciones auxiliares para trabajar con archivos.'''
import copy
import csv
import json
import os
from typing import Any


def ensure_dirs(path: str) -> None:
    '''Crea los directorios necesarios para que la ruta del directorio sea válida.

    Args:
        path:una path absoluta a ser asegurado.'''
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def ensure_file_dirs(path: str) -> None:
    '''Crea los directorios necesarios para que la ruta del archivo sea válida.

    Args:
        path: an absolute path to be ensured.'''
    parent_path = os.path.dirname(path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path, exist_ok=True)


def load_json(path: str, default_value: Any, encoding_format: str = 'utf-8') -> Any:
    ''' Carga el contenido de un archivo json.

    If file no exists creates it with the default value. If there is a problem at decoding it returns default value.

    Args:
        path: an absolute json file path.
        default_value: the value in case of an error.
        encoding_format: the character encoding of the file.
    Returns:
        the object loaded or default value in case of an error.'''
    if not os.path.exists(path):
        save_json(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return copy.deepcopy(default_value)


def save_json(path: str, value: Any, is_custom_class: bool = False, encoding_format: str = 'utf-8') -> None:
    '''Saves an object into a json file.

    Ensures that the path its valid and creates the json version of value to be saved.

    Args:
        path: an absolute json file path.
        value: the object to be saved.
        is_custom_class: if true the json object generated will be value.__dict__ content.
        encoding_format: the character encoding of the file.'''
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else:
            json.dump(value, file, indent=4)


def load_csv(path: str, default_value: list[list[str]], encoding_format: str = 'utf-8', read_only: bool = False) -> list[list[str]]:
    '''Loads the content of a csv file.

    If file no exists:
    - read_only=True: returns the default value.
    - read_only=False: creates it with the default value. If a error occurs at decoding it returns default value.

    Args:
        path: an absolute csv file path.
        default_value: the value in case of an error.
        encoding_format: the character encoding of the file.
        read_only: the mode of the load.
    Returns:
        the csv loaded or default value in case of an error.'''
    if not os.path.exists(path):
        if read_only:
            return copy.deepcopy(default_value)
        save_csv(path, default_value)

    with open(path, mode='r', encoding=encoding_format, newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        try:
            return list(csv_reader)
        except csv.Error:
            return copy.deepcopy(default_value)


def save_csv(path: str, value: list[list[str]], encoding_format: str = 'utf-8') -> None:
    '''Saves a list[list[str]] into a csv file.

    Ensures that path its valid and writes the csv file to be saved.

    Args:
        path: an absolute csv file path.
        value: the csv to be saved.
        encoding_format: the character encoding of the file.'''
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format, newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(value)


def scan_dir(path: str, file_extension: str) -> list[tuple[str, str]]:
    '''Scan a directory and returns a list of name and path for every file finded.

    If path not exists returns an empty list.
    
    Args:
        path: an absolute directory path.
        file_extension: the extension to look for.
    Returns:
        a list of tuple containing the file name and the absolute path to the file.'''
    if not os.path.exists(path):
        return []

    results = [
        (entry.name, entry.path)
        for entry in os.scandir(path) if entry.is_file() and entry.name.endswith(file_extension)
    ]
    return results
