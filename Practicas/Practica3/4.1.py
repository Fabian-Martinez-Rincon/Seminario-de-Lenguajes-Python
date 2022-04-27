import csv
import os.path
import os
path_files = "files"
archivo_net = "BBB_nuevo.csv"

path_arch = os.path.join(os.getcwd(), path_files)

archivo = open(os.path.join(path_arch, archivo_net), "r")
data_net = csv.reader(archivo, delimiter=',')
header , datos = next(data_net), list(data_net )