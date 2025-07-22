"""Cada comando de impresión suele imprimir una
línea propia, con un cambio de línea al final.
 Sin embargo, si se le asigna al comando de
 impresión el argumento adicional end = "",
no imprimirá el cambio de línea.

Corrija este programa para que el cálculo completo,
 con su resultado, se imprima en una sola línea.
   No modifique el número de comandos de impresión
 utilizados."""

"""
print(5)
print(" + ")
print(8)
print(" - ")
print(4)
print(" = ")
print(5 + 8 - 4)
"""

# Fix the code
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

# salida= 5 + 8 - 4 = 9
