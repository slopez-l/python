"""
Escriba un programa que solicite al usuario que escriba un número.
 El programa imprime los enteros positivos entre 1 y el número,
 alternando entre los extremos del rango, como se muestra en los ejemplos a continuación.
 Ejemplo de salida
Escriba un número: 5
1
5
2
4
3
"""

number = int(input("Please type in a number: "))

i = 1
while i <= number:
    if i + 1 <= number:
        print(i + 1)
    print(i)
    i += 2

"""
number = int(input("Please type in a number: "))

for i in range(1, number + 1, 2):
    if i + 1 <= number:
        print(i + 1)
    print(i)
"""
