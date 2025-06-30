"""90.duplicar cada  elemneto de una lista usando map y lambda"""

numeros = [1,2,3,4,5]
duplicados = list(map(lambda x : x * 2, numeros))

print(numeros)
print(duplicados)
