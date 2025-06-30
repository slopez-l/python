"""82.convertir una lista de cadenas
que sean numeros a enteros utilizando map()"""

def convertir_entero(cadena):
    return int(cadena)

cadenas = ["1", "2", "3", "4"]

enteros = list(map(convertir_entero, cadenas))

print(cadenas)
print(enteros)
