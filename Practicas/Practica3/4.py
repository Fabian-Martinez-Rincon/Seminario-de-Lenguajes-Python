import csv
import os



ruta = os.path.dirname(os.path.realpath("."))

path_arch = os.path.join(ruta, "Practica3", "BBB_nuevo.csv")
ruta = os.path.join(path_arch, 'BBB_nuevo.csv')

with open(ruta,"r", encoding="utf-8") as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )
for linea in logs_recurso:
    print(linea[0])