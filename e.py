
vacunados_COVID = {
			'Covishield': [1234567, 9874561, 5632147],
			'Spunik':[3214567, 4563217, 5698743, 9654872], 
			'Sinopharm': [4563287]}
def agregar (vacunados):
	try:
		vacunas = ['Covishield', 'Spunik', 'Sinopharm']
		dni = int(input ('Ingresa DNI'))
		vacuna = int(input ("""Ingresa: 
                    1.- Covishield
                    2.- Spunik
                    3.- Sinpharm """))
		vacunados[vacunas[vacuna-1]].append(dni)
	except (KeyError, IndexError):
		print ('Ojo!! se ingresó una opción de vacuna inválida')	
	finally:
		print ('Los datos se cargaron correctamente')

#Ingreso información vacunados Entidad XX
opcion = input('¿Desea ingresar nuevos vacunados?. S/N: ')
while opcion.upper() == 'S':
	try:
		agregar (vacunados_COVID)
	except:
		print ('Ups!.. hubo un problema!..')
	opcion = input('¿Desea ingresar nuevos vacunados?. S/N: ')
	
print ('Listado de los vacunados hasta hoy: ', vacunados_COVID)
