"""33.dertermina si un año es bisiestro
	regla de negocio
		- Divisible por 4.
		- no divisible por 100.
		- Divisible por 400
		"""

año = 2023

if (año % 4 == 0 and año % 100 != 0) or \
	(año % 400 == 0):
	print("es un año bisiesto")
else:
	print("no es bisiesto")
