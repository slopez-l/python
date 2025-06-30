"""93.filtrar numeros negativos de una lista utilizando filter"""

numeros = [-3,1,-5,8,-42]

negativos = list(filter(lambda x:x < 0, numeros))

print(numeros)
print(negativos)
