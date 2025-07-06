"""49.simular el lanzamiennto de un dado hasta obtener 6"""

import random

while True:
    dado = random.randint(1, 6)
    if dado == 1:
        print("a salido 1")
    elif dado == 2:
        print("a salido 2")
    elif dado == 3:
        print("a salido 3")
    elif dado == 4:
        print("a salido 4")
    elif dado == 5:
        print("a salido 5")
    else:
        print("a salido 6")
    jugar = input("tirar de nuevo (S/N)")
    if jugar == "n":
        break
print("gracias por jugar")
