"""59.pedir al usuario un numero
 e imprimir la tabla de multiplicar del mismo"""

numero = int(input("escibeme un numero"))

for i in range(1, 11):
	resultado = numero * i
	print(f"{ numero } x {i} = { resultado }")
