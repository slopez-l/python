"""Escriba un programa que solicite al usuario números enteros.
 El programa debe seguir solicitando números hasta que el usuario escriba cero.

Ejemplo de salida
Escriba números enteros. Escriba 0 para finalizar.
Número: 5
Número: 22
Número: 9
Número: -2
Número: 0

Parte 1: Conteo
Después de leer los números, el programa debe mostrar cuántos números
se escribieron. El cero final no debe incluirse en el conteo.

Necesitará una nueva variable para registrar los números ingresados.

Ejemplo de salida
... el programa solicita números
Números ingresados: 4

Parte 2: Suma
El programa también debe mostrar la suma de todos los números ingresados.
 El cero final no debe incluirse en el cálculo.

El programa debería mostrar lo siguiente:

Ejemplo de salida
... el programa solicita números
Números ingresados: 4
La suma de los números es 34

Parte 3: Media
El programa también debería mostrar la media de los números.
 El cero final no debe incluirse en el cálculo. Se puede asumir
 que el usuario siempre escribirá al menos un número válido distinto de cero.

Ejemplo de salida
... el programa solicita números
Números ingresados: 4
La suma de los números es 34
La media de los números es 8.5

Parte 4: Positivos y negativos
El programa también debería mostrar estadísticas sobre cuántos números
fueron positivos y cuántos negativos. El cero final no debe incluirse
 en el cálculo.

Ejemplo de salida
... el programa solicita números
Números ingresados: 4
La suma de los números es 34
La media de los números es 8.5
Números positivos: 3
Números negativos: 1"""


print("Please type in integer numbers. Type in 0 to finish.")

contador = 0
suma = 0
positivos = 0
negativos = 0

while True:
    number = int(input("Number:"))
    if number == 0:
        break
    contador += 1
    suma += number

    if number > 0:
        positivos += 1
    elif number < 0:
        negativos += 1

print(f"Numbers typed in {contador}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {suma / contador:.1f}")
print(f"Positive numbers {positivos}")
print(f"Negative numbers {negativos}")
