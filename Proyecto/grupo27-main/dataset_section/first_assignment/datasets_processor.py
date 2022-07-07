import os
import csv
UPPER_GENDERS_SPOTIFY = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]
ORDEN_SPOTIFY = ["Top Genre", "Artist Type", "Year Released", "Top Year", "BPM" ,"Artist"]
ORDEN_LAGOS = ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"]
ORDEN_FIFA21 = ["Team", "Nationality", "Position", "Age", "Potential" ,"Name"]
ALL_ORDEN_REMOVE = [ORDEN_SPOTIFY,ORDEN_LAGOS,ORDEN_FIFA21]

NAMES_REMOVE_SPOTIFY = ["Top Genre", "Year Released","BPM", "Top Year", "Artist Type","Artist"]
NAMES_REMOVE_LAGOS = ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"]
NAMES_REMOVE_FIFA21 = ["Age", "Nationality", "Position", "Team" , "Potential","Name"]
ALL_NAMES_REMOVE = [NAMES_REMOVE_SPOTIFY,NAMES_REMOVE_LAGOS,NAMES_REMOVE_FIFA21]

NAMES_DATASETS = ["Spotify_2010-2019_Top_100.csv","Lagos_Argentina - Hoja_1.csv","FIFA-21_Complete.csv"]

path = os.path.dirname(os.path.realpath("."))

#def all_path_function():
#def archive_process():

def data_process(path:str):
    """Separa los datos_spotify del archivo 
    """
    all_header:list[list[str]] = [] #Guardo todos los encabezados
    all_datos: list[list[list[str]]]= []
    all_path_file:list[str] = []
    [all_path_file.append(os.path.join(path,"grupo27","dataset_section","base_datasets",NAMES_DATASETS[index])) for index in range(0,len(NAMES_DATASETS))]
    for index in range(0,len(all_path_file)):
        with open(all_path_file[index],"r", encoding="utf-8") as File:  
            if not(index == 2):
                csv_reader = csv.reader(File, delimiter=',')
            else:
                csv_reader = csv.reader(File, delimiter=';')
            all_header.append(next(csv_reader)) # El encabezado para comparar las columnas borradas
            all_datos.append(list(csv_reader))
    return all_header,all_datos
all_header,all_datos = data_process(path)

def create_order(orden_list:list[int],name_remove:list[str],header:list[str]):
    # Columnas para invertir datos_spotify
    """Crea un orden a partir de dos listas.\n
    Ej: hola, chau, bye\n
    [0, 1, 2]\n
    Y queremos que este en este orden\n
    Ej: bye, hola, chau\n
    Genera una lista con:\n
    [2, 0, 1]
    """
    names_compare = list(map(lambda x: x.lower(), name_remove))
    header_compare = list(map(lambda x: x.lower(), header))
    for name in names_compare:
        for pos,dato in enumerate(header_compare):
            if (name == dato):
                orden_list.append(pos)

def separate_cols(all_cols_remove:list[list[int]],all_header:list[list[str]]):
    """Separa las columnas de las que quiero eliminar
    """
    for index,name_remove in enumerate(ALL_NAMES_REMOVE):
        cols_remove:list[int] = []
        names_compare = (list(map(lambda x: x.lower(), name_remove))) # Creamos una lista para comparar
        header = all_header[index]
        for column in header:    # Recorro el encabezado actual
            if not(column.lower() in names_compare):
                index_dato = header.index(column)
                cols_remove.append(index_dato)
        all_cols_remove.append(cols_remove)
all_cols_remove:list[list[int]] = []  # Columnas que voy a eliminar [0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]  
separate_cols(all_cols_remove,all_header)



def cols_sorted(row:list[str],orden_list:list[int]): # [0, 1, 2, 3, 4, 5]
    """Intercambialas posiciones de una lista
    """
    row_copia = row.copy()
    for indice,dato in enumerate(orden_list):        # [1, 5, 2, 4, 3, 0]    
        row[indice]= row_copia[dato]                       
    return row

def upper_words(word:str):
    """Procesa una frase dependiendo de la consigna"""
    genders = word.split()
    for index, gender in enumerate(genders):
        if gender.upper() in UPPER_GENDERS_SPOTIFY:
            genders[index]= gender.upper()
        else:
            genders[index]= gender.title()
    word = " ".join(genders)
    return word

def cols_remove_function(row:list[str],cols_remove:list[int]):
    """Elimina posiciones de una lista (las posiciones son pasadas por parametro)"""
    for col_index in cols_remove:
        del (row[col_index])
    return row

for index,col in enumerate(all_cols_remove):
    all_cols_remove[index] = sorted(col, reverse=True) # En reverso para sacar primero las columnas desde el final

def first_order(NewFile):
    csv_writer = csv.writer(NewFile)
    header_orden = all_header[index].copy()
    cols_remove_function(header_orden,all_cols_remove[index])
    orden_list:list[int] = []  
    create_order(orden_list,ALL_ORDEN_REMOVE[index],header_orden)
    return csv_writer,orden_list

for index,name_dataset in enumerate(NAMES_DATASETS):
    path_newfile = os.path.join(path,"grupo27", "dataset_section", "processed_datasets", name_dataset)
    with open(path_newfile, "w",encoding="utf-8",newline='') as NewFile:
        csv_writer,orden_list=first_order(NewFile)
        all_datos[index].insert(0,all_header[index]) 
        print(orden_list)
        if (index == 0): # Spoty
            for row in all_datos[index]:
                row[2] = upper_words(row[2])
                row = cols_remove_function(row,all_cols_remove[index])
                row = cols_sorted(row,orden_list)
                csv_writer.writerow(row)
        if (index == 1): # Lagos
            for row in all_datos[index]:
                row[2] = upper_words(row[2])
                row = cols_remove_function(row,all_cols_remove[index])
                row = cols_sorted(row,orden_list)
                csv_writer.writerow(row)
        if (index == 2): # Fifa
            for row in all_datos[index]:
                row[2] = upper_words(row[2])
                row = cols_remove_function(row,all_cols_remove[index])
                row = cols_sorted(row,orden_list)
                csv_writer.writerow(row)