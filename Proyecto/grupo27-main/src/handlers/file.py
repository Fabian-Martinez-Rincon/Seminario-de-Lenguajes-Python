'''Contains helper functions to work with files.'''
import copy
import csv
import json
import os
from typing import Any


def ensure_dirs(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def ensure_file_dirs(path: str) -> None:
    parent_path = os.path.dirname(path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path, exist_ok=True)


def load_json(path: str, default_value: Any, encoding_format: str = 'utf-8') -> Any:
    if not os.path.exists(path):
        save_json(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return copy.deepcopy(default_value)


def save_json(path: str, value: Any, is_custom_class: bool = False, encoding_format: str = 'utf-8') -> None:
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else:
            json.dump(value, file, indent=4)


def load_csv(path: str, default_value: list[list[str]], encoding_format: str = 'utf-8', read_only: bool = False) -> list[list[str]]:
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
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format, newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(value)


def scan_dir(path: str, file_extension: str | None = None) -> list[tuple[str, str]]:
    if not os.path.exists(path):
        return []

    if file_extension is None:
        results = [(entry.name, entry.path) for entry in os.scandir(path)]
    else:
        results = [
            (entry.name, entry.path)
            for entry in os.scandir(path) if entry.is_file() and entry.name.endswith(file_extension)
        ]
    return results
