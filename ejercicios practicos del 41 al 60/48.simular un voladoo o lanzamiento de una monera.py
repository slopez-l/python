"""48.simular un voladoo o lanzamiento de una monera"""

import random

while True:
    moneda = random.randint(1, 2)
    if moneda == 1:
        print("cara")
    else:
        print("cruz")
    jugar = input("tirar de nuevo (S/N)")
    if jugar.lower() == "n":
        break
print("gracias por jugar")
