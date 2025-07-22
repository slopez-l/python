limit = int(input("limit:"))
number = 1
suma = 0
operacion =""

while suma < limit:
    suma += number
    if operacion == "":
        operacion = str(number)
    else:
        operacion += f" + {number}"
    number += 1

print(f"The consecutive sum: {operacion} = {suma}")
