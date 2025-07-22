"""
Escriba un programa que encuentre la segunda ocurrencia de una subcadena.
 Si no hay una segunda (o primera) ocurrencia, el programa debería mostrar un mensaje correspondiente.

En este ejercicio, las ocurrencias no pueden superponerse.
 Por ejemplo, en la cadena aaaa, la segunda ocurrencia de la subcadena aa está en el índice 2.
"""

string = input("Please type in a string:")
substring = input("Please type in a substring:")

# Busca la primera aparición de la subcadena en la cadena principal
# Si no la encuentra, 'first' será igual a -1
first = string.find(substring)

# Si se encontró una primera aparición, busca la segunda comenzando justo después del final de la primera
# Si no se encontró ninguna primera aparición, 'second' se asigna directamente como -1
#(find()=devuelve el indice siencontro el valos y si no lo encontro -1)
second = string.find(substring, first + len(substring)) if first != -1 else -1

# Si 'second' es distinto de -1, significa que se encontró una segunda aparición válida
if second != -1:
    # Imprime la posición (índice) donde empieza esa segunda aparición
    print(f"The second occurrence of the substring is at index {second}.")
else:
    # Si no se encontró una segunda aparición, se muestra este mensaje estándar
    print("The substring does not occur twice in the string.")

"""
salida:
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.
"""
