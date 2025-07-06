"""46.solicita al usuario ingresar un numero
 y cuenta cuantos digitos tiene"""

numero = int(input("ingresa un numero = "))
contador = 0
while numero != 0:
    numero = numero // 10  # division entera
    contador = contador + 1
print("digitos son ", contador)
