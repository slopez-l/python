string = input("Please type in a string: ")
# Calcula el último índice de la cadena
#   (ya que los índices empiezan en 0).

index = len(string) - 1
# El bucle se repite mientras el índice sea igual o mayor a 0
#   (recorriendo hacia atrás).
while index >= 0:
    # Imprime el carácter en la posición actual del índice
    print(string[index])
    # Disminuye el valor del índice para pasar al
    #   carácter anterior en la siguiente vuelta.
    index -= 1

"""
Please type in a string: gato
o
t
a
g
"""
