"""69.escribe una funcion para calcular la tasa de desempleo
td = no_empleados/fuerza_laboralx100"""

def tasa_desempleo(no_em, si_em):
	return(no_em / si_em) * 100

resulatdo = tasa_desempleo(100, 900)

print(resulatdo)
