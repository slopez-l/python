"""81.elavar al cuadrado una lista de numeros utilizando map()"""

def cuadrado(x):
    return x ** 2

numeros = [1,2,3,4,5]
cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(cuadrados)
