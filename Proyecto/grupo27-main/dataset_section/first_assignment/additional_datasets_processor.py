import csv
import os
from typing import Callable


RowTransformFn = Callable[[list[str]], list[str]]


def transform_csv(
    source_path: str, result_path: str,
    header_fn: RowTransformFn, content_fn: RowTransformFn,
    source_value_delimiter: str = ',',
    contains_header: bool = True, remove_header: bool = False,
    remove_empty_lines: bool = True
) -> None:
    with (
        open(source_path, mode='r', encoding='utf-8') as src_file,
        open(result_path, mode='w', encoding='utf-8') as res_file
    ):
        reader = csv.reader(src_file, delimiter=source_value_delimiter)
        writer = csv.writer(res_file, delimiter=',', lineterminator='\n')
        if contains_header:
            header = next(reader)
            if not remove_header:
                writer.writerow(header_fn(header))
        for row in reader:
            if remove_empty_lines and row.count('') == len(row):
                continue
            transformed_row = content_fn(row)
            writer.writerow(transformed_row)


def row_resample_factory(index_sequence: list[int]) -> RowTransformFn:
    def resample(original: list[str]) -> list[str]:
        return [original[index] for index in index_sequence]

    return resample


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
SRC_PATH = os.path.join(BASE_PATH, 'base_datasets')
OUTPUT_PATH = os.path.join(BASE_PATH, 'processed_datasets')

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)


# Spotify dataset

spotify_resample = row_resample_factory([2, 16, 3, 15, 5, 1])

MUSICAL_ACRONYMS = ('EDM', 'DFW', 'UK', 'R&B', 'LGBTQ+')


def spotify_header(row:list[str]) -> list[str]:
    return [
        'Top genero', 'Tipo artista', 'Año lanzamiento',
        'Mejor año', 'BPM', 'Artista'
    ]


def restyle_gender(word: str) -> str:
    if word.upper() in MUSICAL_ACRONYMS:
        word = word.upper()
    else:
        word = word.title()
    return word


def spotify_content(row: list[str]) -> list[str]:
    new_values = spotify_resample(row)
    gender_words = new_values[0].split()
    new_values[0] = ' '.join([restyle_gender(word) for word in gender_words])
    return new_values


transform_csv(
    os.path.join(SRC_PATH, 'Spotify_2010-2019_Top_100.csv'),
    os.path.join(OUTPUT_PATH, 'spotify.csv'),
    spotify_header,
    spotify_content
)


# Lakes dataset

lakes_resample = row_resample_factory([1, 2, 3, 4, 5, 0])


def dms_to_dd(coord: str, n_decimals: int = 5) -> str:
    sign = -1 if 'S' in coord or 'O' in coord else 1
    degree, coord = coord[:-2].split('°')
    min, sec = coord.split('\'')
    dd = sign * (int(degree) + int(min)/60 + int(sec)/3600)
    return str(round(dd, n_decimals)) + '°'


def lakes_content(row: list[str]) -> list[str]:
    new_values = lakes_resample(row)
    for pos, value in enumerate(new_values):
        if not value:
            new_values[pos] = 'Desconocido'
    latitude, longitude = new_values[4].split()
    new_values[4] = dms_to_dd(latitude) + ' ' + dms_to_dd(longitude)
    return new_values


transform_csv(
    os.path.join(SRC_PATH, 'Lagos_Argentina - Hoja_1.csv'),
    os.path.join(OUTPUT_PATH, 'lakes.csv'),
    lakes_resample,
    lakes_content
)


# FIFA dataset

fifa_resample = row_resample_factory([8, 2, 3, 5, 7, 1])

POTENTIAL_TABLE = {
    90: 'Sobresaliente',
    80: 'Muy bueno',
    60: 'Bueno',
    -1: 'Regular'
}

POSITION_TABLE = {
    'ST': 'Delantero',
    'CM': 'Volante',
    'CDM': 'Medio centro defensivo',
    'LB': 'Lateral izquierdo',
    'GK': 'Portero',
    'LM': 'Volante izquierdo',
    'RM': 'Volante derecho',
    'CAM': 'Volante ofensivo',
    'LW': 'Extremo izquierdo',
    'LWB': 'Lateral izquierdo ofensivo',
    'CB': 'Defensor central',
    'RB': 'Lateral derecho',
    'RW': 'Extremo derecho',
    'RWB': 'Lateral ofensivo derecho',
    'CF': 'Media punta'
}


def fifa_header(row:list[str]) -> list[str]:
    return [
        'Equipo', 'Nacionalidad', 'Posición',
        'Edad', 'Potencial', 'Nombre'
    ]


def fifa_content(values: list[str]) -> list[str]:
    new_values = fifa_resample(values)
    potential = int(new_values[4])
    for value in POTENTIAL_TABLE:
        if potential >= value:
            new_values[4] = POTENTIAL_TABLE[value]
            break
    positions = new_values[2].split('|')
    full_positions = '|'.join([POSITION_TABLE[acronym] for acronym in positions])
    new_values[2] = full_positions
    return new_values


transform_csv(
    os.path.join(SRC_PATH, 'FIFA-21_Complete.csv'),
    os.path.join(OUTPUT_PATH, 'fifa.csv'),
    fifa_header,
    fifa_content,
    source_value_delimiter=';'
)
