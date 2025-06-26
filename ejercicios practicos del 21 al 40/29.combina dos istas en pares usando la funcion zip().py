"""29.combina dos istas en pares usando la funcion zip()"""

lista1 = [1,2,3]
lista2 = ["a","b","c"]
 #genera pares teninedo en cunta el indice de cada lista
pares = list(zip(lista1, lista2))

print(pares)	#[(1, 'a'), (2, 'b'), (3, 'b')]
