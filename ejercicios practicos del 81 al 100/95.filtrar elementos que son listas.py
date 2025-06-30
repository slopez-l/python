"""95.filtrar elementos que son listas"""

lista1 = [1, 2 ,[3,4], ["a", "b"], 5]
#hace que devuelva las listas dentro de otras listas
listas = list(filter(lambda x: isinstance(x, list), lista1))

print(lista1)
print(listas)
