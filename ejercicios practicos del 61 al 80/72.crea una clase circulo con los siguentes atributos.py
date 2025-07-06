"""72.crea una clase circulo con los siguentes atributos:
* radio : radio circulo
la clase debe tener los siguientes metodos:
* __init__(self, radio) : ininializa los
atributos de la clase.
* calcular_area(self): calcula y
develve el area del circulo
* clacular_perimetro(self): calcula y
devuelve el perimetro del circulo"""


import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


circulo1 = Circulo(5)

print(f"el area es : {circulo1.calcular_area()}")
print(f"perimetro: {circulo1.calcular_perimetro()}")
