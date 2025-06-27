"""50.mostrar los numeros del 1 al 100
pero reemplazando los multipolos de 3 por "Fizz"
y los multiplos de 5 por "Buzz"""

i = 1
while i <= 100:
	if i % 3 == 0 and i % 5 == 0:
		print("Fizzbuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)
	i = i + 1


