"""
Word: testing

******************************
*          testing           *
******************************
"""
word = input("Word:")
longitud = 30

linea_superior = "*" * longitud
print(linea_superior)

# Centra la palabra en longitud - 2 y añade asteriscos en los extremos
centro = word.center(longitud - 2)
print(f"*{centro}*")

linea_inferior = "*" * longitud
print(linea_inferior)
