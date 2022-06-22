import os
import pandas as pd

POTENTIAL_TABLE_FIFA = {
    90: 'Sobresaliente',
    80: 'Muy bueno',
    60: 'Bueno',
    -1: 'Regular'
}

POSITION_TABLE_FIFA = {
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

UPPER_GENDERS_SPOTIFY = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]


def potential_replace(potential):
    compare_potential = int(potential)
    for potential_player in POTENTIAL_TABLE_FIFA:
        if compare_potential >= potential_player:
            potential = POTENTIAL_TABLE_FIFA[potential_player]
            break
    return potential


def position_replace(position):
    positions = position.split('|')
    position = '|'.join([POSITION_TABLE_FIFA[acronym]
                        for acronym in positions])
    return position


def upper_words(sentence):
    """Procesa una frase dependiendo de la consigna"""
    genders = sentence.split()
    for index, gender in enumerate(genders):
        genders[index] = (gender.upper() if gender.upper()
                          in UPPER_GENDERS_SPOTIFY else gender.title())
    sentence = " ".join(genders)
    return sentence


def rebase_coord(coord, n_decimals=5):
    sign = -1 if 'S' in coord or 'O' in coord else 1
    degree, coord = coord[:-2].split('°')
    min, sec = coord.split('\'')
    dd = sign * (int(degree) + int(min)/60 + int(sec)/3600)
    return str(round(dd, n_decimals)) + '°'


def transform_coords(coords):
    latitude, longitude = coords.split()
    coords = rebase_coord(latitude) + ' ' + rebase_coord(longitude)
    return coords


DATASETS = {
    'FIFA-21_Complete.csv': {
        'order': ["team", "nationality", "position", "age", "potential", "name"],
        'translation': ['Equipo', 'Nacionalidad', 'Posición', 'Edad', 'Potencial', 'Nombre'
                        ],
        'functions': {
            "potential": potential_replace,
            "position": position_replace
        },
        'name': "fifa.csv"
    },
    'Lagos_Argentina - Hoja_1.csv': {
        'order': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas", "Nombre"],
        'functions': {
            "Coordenadas": transform_coords
        },
        "name": 'lakes.csv'
    },
    'Spotify_2010-2019_Top_100.csv': {
        'order': ["top genre", "artist type", "year released", "top year", "bpm", "artist"],
        'translation': ['Top genero', 'Tipo artista', 'Año lanzamiento', 'Mejor año', 'BPM', 'Artista'],
        'functions': {
            "top genre": upper_words
        },
        'name': 'spotify.csv'
    }
}

PATH_BASE = os.path.dirname(os.path.dirname(__file__))
PATH_SOURCE = os.path.join(PATH_BASE, "base_datasets")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_datasets")
if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)


def process_dataset(file_name):
    if file_name not in DATASETS:
        return
    file_path = os.path.join(PATH_SOURCE, file_name)
    config = DATASETS[file_name]
    processed_path = os.path.join(PATH_PROSSED, config['name'])
    try:
        with open(file_path, mode='r', encoding="UTF-8") as file:
            df = pd. read_csv(file, sep=None, engine="python",
                              usecols=(config['order']), dtype=str,error_bad_lines=False)
    except FileNotFoundError:
        print('No existe la ruta', PATH_SOURCE)
        return
    df.dropna(how="all", inplace=True)

    df = df[config['order']]

    for columna, function in config['functions'].items():
        df[columna] = df[columna].apply(function)
    df.fillna('Desconocido',  inplace=True)

    df.to_csv(processed_path, mode='w', index=False)


try:
    names_files = os.listdir(PATH_SOURCE)
except (FileNotFoundError, NotADirectoryError) as error:
    match error:
        case FileNotFoundError():
            print('No existe la ruta', PATH_SOURCE)
        case NotADirectoryError():
            print('La ruta no es un directorio ', PATH_SOURCE)
    names_files = []


for file_name in names_files:
    process_dataset(file_name)
