"""96.crear una excepcion que me ayude a determinar
si el indice de una lisa esta fuera de rango"""

mi_lista = [1,2,3]

try:
    print(mi_lista[5])
except IndexError:
    print("Error, el indice no existe")
