"""68.escibe una funcion que pidapor teclado la distancia
 y la velocidad para poder calcular el tiempo del viaje"""

def tiempo_viaje():
	distancia = int(input("escibe la distancia"))
	velocidad = int(input("escibe la velocidad"))

	return distancia / velocidad

resultado = tiempo_viaje()
print(resultado, "horas")
