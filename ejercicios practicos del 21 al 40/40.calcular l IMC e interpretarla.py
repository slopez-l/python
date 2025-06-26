"""40.calcular l IMC e interpretarla"""

peso = 70
altura = 1.75

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
	print("bajo peso")
elif imc < 25:
	print("normal")
elif imc < 30:
	print("sobrepeso")
elif imc < 35:
	print("obesidad grado 1")
elif imc < 40:
	print("obesidad grado 2")
else
	print("obesidad grado 3")
