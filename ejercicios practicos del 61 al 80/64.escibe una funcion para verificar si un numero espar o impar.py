"""64.escibe una funcion para verificar
 si un numero espar o impar"""

def es_par(numero):
	if numero % 2 == 0:
		return True
	else:
		return False
resultado = es_par(8)
print(resultado)
