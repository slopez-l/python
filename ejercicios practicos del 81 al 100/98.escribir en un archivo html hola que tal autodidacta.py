"""98.escribir en un archivo html hola que tal autodidacta"""

def escribir(nombre_archivo, contenido):
	with open(nombre_archivo, "w") as archivo:
		archivo.write(contenido)

escribir("index.html", "hola que tal autodidacta")
