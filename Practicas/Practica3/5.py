import csv
from operator import length_hint
import os
from datetime import date
import datetime 
import calendar
from collections import Counter

def findDay(fecha:str): 
    born = datetime.datetime.strptime(fecha,"%d/%m/%Y %H:%M").weekday() 
    return (calendar.day_name[born]) 

#3/03/2022 07:22

ruta = os.path.dirname(os.path.realpath("."))

path_arch = os.path.join(ruta, "Practica3")
ruta = os.path.join(path_arch, 'BBB_nuevo.csv')

with open(ruta,"r", encoding="utf-8") as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )

dias_semanales:list[str]

print(logs_recurso[0][0])
fechas = logs_recurso[0][0].split('/')
dia = int(fechas[0])
mes = int(fechas[1])
anio = int(fechas[2][0:4])

a = datetime.datetime(anio, mes, dia, 00, 00) 

fechas2 = logs_recurso[len(logs_recurso)-1][0].split('/')
dia2 = int(fechas2[0])
mes2 = int(fechas2[1])
anio2 = int(fechas2[2][0:4])

b = datetime.datetime(anio2, mes2, dia2, 00, 00) 
c = a-b  
print('Difference: ', c) 
  
