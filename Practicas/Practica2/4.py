from cgitb import text
from posixpath import split
from time import process_time_ns

texto = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
syste"""

list_valores  = [0,0,0,0]
titulo = (((texto.split("\n")[0])).split()) #Saco el titulo
titulo.remove(titulo[0]) #Elimino el primer elemento que no cuenta para el titulo
if (len(titulo)<=10):
    print("Titulo esta ok")

oraciones = texto.split(".")
oraciones.remove(oraciones[0]) #Elimino el titulo

for oracion in oraciones:
    if (len((oracion).split()) <= 12):
        list_valores [0]+=1
    elif((len((oracion).split()) >= 13) & (len((oracion).split()) <=17) ): 
        list_valores [1]+=1
    elif((len((oracion).split())>= 18) & (len((oracion).split()) <=25) ): 
        list_valores [2]+=1
    elif (len((oracion).split())>25):
        list_valores [3]+=1

print("Cantidad de oraciones fáciles de leer:", list_valores[0]," aceptables para leer:", list_valores[1], "dificil de leer: ",list_valores[2]," muy dificil de leer:" ,list_valores[3])