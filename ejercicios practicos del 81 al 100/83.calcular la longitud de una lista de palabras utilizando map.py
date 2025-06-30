"""83.calcular la longitud de una lista de palabras utilizando map"""


def longitud(palabra):
    return len(palabra)

palabras = ["gato", "perro", "aguilajkjk"]

longitudes = list(map(longitud, palabras))

print(palabras)
print(longitudes)


