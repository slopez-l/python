"""solicita al usuario ingresar un numero y
luego imprime la suma de todos los numeros desde 1 hasta N"""

numero = int(input("escibe un numero"))
suma = 0
i = 1
while i <= numero:
	suma += i
	i += 1
print("la suma es ", suma)
