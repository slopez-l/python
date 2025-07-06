"""67.escibe una funcion para calcular el volumen de un cilindro
V = πr^2h  """


import math


def volumen_cilindro(radio, altura):

    return math.pi * radio ** 2 * altura


resulatdo = volumen_cilindro(3, 5)
print(resulatdo)
