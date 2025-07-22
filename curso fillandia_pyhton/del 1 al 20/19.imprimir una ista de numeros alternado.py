"""Escriba un programa que solicite al usuario que escriba un número.
 El programa imprime todos los valores enteros positivos desde 1 hasta el número.
   Sin embargo, el orden de los números se cambia para que cada par de números se invierta.
     Es decir, el 2 va antes del 1, el 4 antes del 3, y así sucesivamente.
       Consulte los ejemplos a continuación para obtener más información.

Ejemplo de salida
Escriba un número: 5
2
1
4
3
5
"""

# Se pide al usuario un número entero
number = int(input("Please type in a number: "))

# Se inicializa la variable i con valor 1 (comenzamos desde el extremo inferior)
i = 1

# Mientras i sea menor o igual al número dado
while i <= number:

    # Si hay al menos un número más disponible después de i (para evitar pasarse del límite)
    if i + 1 <= number:
        print(i + 1)  # Se imprime primero el número superior del par

    print(i)  # Luego se imprime el número inferior del par

    # Se incrementa i en 2 para avanzar al siguiente par
    i += 2


"""
# Pedimos al usuario que introduzca un número entero
number = int(input("Please type in a number: "))

# Recorremos los números desde 1 hasta 'number', avanzando de 2 en 2 (es decir, solo los impares)
for i in range(1, number + 1, 2):

    # Si existe un número siguiente (i + 1) que esté dentro del límite
    if i + 1 <= number:
        print(i + 1)   # Imprime el número siguiente (el par)

    print(i)           # Imprime el número actual (el impar que viene del bucle)

"""
