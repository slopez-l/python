"""43bis con while.solicitaal usuario ingresar  un numero n
 e imprime el factorial de ese numero"""


numero = n = int(input("ingresa un numero = "))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i = i + 1
print("el factorial es = ", factorial)
