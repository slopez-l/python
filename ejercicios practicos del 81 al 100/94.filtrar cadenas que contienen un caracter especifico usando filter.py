"""94.filtrar cadenas que contienen
 un caracter especifico usando filter"""

cadenas = ["apple", "python", "hola"]
caracter = "a"

con_a = list(filter(lambda x:caracter in x, cadenas))

print(cadenas)
print(con_a)
