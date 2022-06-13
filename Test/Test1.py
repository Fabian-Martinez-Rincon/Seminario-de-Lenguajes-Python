# Módulo: mis_funciones
def calcular_promedio(lista):
	""" Calcula el promedio de los valores dentro de la lista dada como argumento"""
	cant_elementos = len(lista)
	return 0 if cant_elementos == 0 else sum(lista)/cant_elementos
#Código: test1.py
import unittest
from mis_funciones import calcular_promedio
class TestMiFuncion(unittest.TestCase):
	def test_case1(self):
		""" Testea que el promedio de una lista vacía de 0"""
		self.assertEqual(calcular_promedio([]), 0)
	def test_case2(self):
		""" Testea que el promedio de una lista con un único valor es el mismo valor """
		valor = 1
		self.assertEqual(calcular_promedio([valor]), float(valor))
	def test_case3(self):
		""" testea que el promedio de los valores 1, 2 y 3 sea 2.0"""

		self.assertEqual(calcular_promedio([1, 2, 3]), 2.0)
if __name__ == '__main__':
	unittest.main()