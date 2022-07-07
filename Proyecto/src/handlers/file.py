'''Contains helper functions to work with files.'''
import copy
import csv
import json
import os
from typing import Any
# Tipo especial que indica un tipo sin restricciones.
# Todos los tipos son compatibles con Any.
# Any es compatible con todos los tipos


def ensure_dirs(path: str) -> None:
    '''Crea los directorios necesarios para que la ruta del directorio sea válida.
    Args:
        path: an absolute path to be ensured/asegurado.''' 
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def ensure_file_dirs(path: str) -> None:
    '''Crea los directorios necesarios para que la ruta del archivo sea válida.
    Args:
        path: an absolute path to be ensured.'''
    parent_path = os.path.dirname(path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path, exist_ok=True)


def load_json(path: str, default_value: Any, encoding_format: str = 'utf-8') -> Any: # la codificación de caracteres del archivo
    '''Loads the content of a json file.

    If file no exists creates it with the default value. If there is a problem at decoding it returns default value.

    Args:
        path: an absolute json file path.
        default_value: el valor en caso de error.
        encoding_format: the character encoding of the file.
    Returns:
        el objeto cargado o el valor por defecto en caso de error.'''
    if not os.path.exists(path):
        save_json(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        try:
            return json.load(file)
        except json.JSONDecodeError: # indica que hay un problema con la forma en que se formatean los datos JSON. Por ejemplo, es posible que a sus datos JSON les falte un corchete, o tengan una clave que no tenga un valor, o les falte alguna otra parte de la sintaxis.
            return copy.deepcopy(default_value)
# La diferencia entre copy() y deepcopy() solo es relevante para objetos compuestos (objetos que contienen otros objetos, como listas o instancias de clase)
# El copy() solo copia los primeros niveles
# https://docs.python.org/3/library/copy.html#copy.deepcopy

def save_json(path: str, value: Any, is_custom_class: bool = False, encoding_format: str = 'utf-8') -> None:
    '''Saves an object into a json file.
    Se asegura de que la ruta sea válida y crea la versión json del valor que se guardará.
    Args:
        path: an absolute json file path.
        value: the object to be saved.
        is_custom_class: if true the json object generated will be value.__dict__ content.
        encoding_format: the character encoding of the file.'''
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else: # que convierte los objetos de Python en objetos json apropiados.
            json.dump(value, file, indent=4) # El método dump() se usa cuando los objetos de Python deben almacenarse en un archivo


def load_csv(path: str, default_value: list[list[str]], encoding_format: str = 'utf-8', read_only: bool = False) -> list[list[str]]:
    '''Loads the content of a csv file.

    If file no exists:
    - read_only=True: returns the default value.
    - read_only=False: lo crea con el valor por defecto. Si se produce un error al decodificar, devuelve el valor predeterminado.

    Args:
        path: an absolute csv file path.
        default_value: the value in case of an error.    ¿porque me guardo los valores en caso de error?
        encoding_format: the character encoding of the file.
        read_only: el modo de la carga.
    Returns:
        the csv loaded or default value in case of an error.'''
    if not os.path.exists(path):
        if read_only:                               # Si es true retorno los valores como estan (retornamos la copia para estar seguros de no tener problemas con enlases)
            return copy.deepcopy(default_value)
        save_csv(path, default_value)
    # Como me aseguro de que mi ruta existe, y puedo abrirlo
    with open(path, mode='r', encoding=encoding_format, newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        try:
            return list(csv_reader)         # el csv cargado 
        except csv.Error:
            return copy.deepcopy(default_value) # o el valor predeterminado en caso de error.


def save_csv(path: str, value: list[list[str]], encoding_format: str = 'utf-8') -> None:
    '''Saves a list[list[str]] into a csv file.
    Se asegura de que la ruta sea válida y escribe el archivo csv para guardarlo.
    Args:
        path: an absolute csv file path.
        value: the csv to be saved.
        encoding_format: the character encoding of the file.'''
    ensure_file_dirs(path)
    with open(path, mode='w', encoding=encoding_format, newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(value)


def scan_dir(path: str, file_extension: str | None = None) -> list[tuple[str, str]]:
    '''Escanea un directorio y devuelve una lista de nombres y rutas para cada archivo encontrado..
    Si la ruta no existe, devuelve una lista vacía.
    
    Args:
        path: an absolute directory path.
        file_extension: the extension to look for.
    Returns:
        a list of tuple containing the file name and the absolute path to the file.'''
    if not os.path.exists(path):
        return []

    if file_extension is None:
        results = [(entry.name, entry.path) for entry in os.scandir(path)]
    else:
        results = [
            (entry.name, entry.path)
            for entry in os.scandir(path) if entry.is_file() and entry.name.endswith(file_extension) 
        ]# endswith : devuelve True si una cadena termina con el sufijo dado; de lo contrario, devuelve False.
    return results
