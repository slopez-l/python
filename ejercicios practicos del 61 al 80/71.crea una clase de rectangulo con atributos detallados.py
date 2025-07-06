"""71.crea una clase de rectangulo con los siguenntes atributos:
base : base rectangulo
altura : altura rectangulo
la clase debe tener los siguientes metodos:
** __init__(self, base, altura):inizializa los
atribulos de la clase.
** calcular_area(self): calcula y
develve el area del rectangulo
** clacular_perimetro(self): calcula y
devuelve el perimetro del rectangulo"""


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


rectangulo1 = Rectangulo(5, 3)

print(f"Area: {rectangulo1.calcular_area()}")
print(f"Perimetro: {rectangulo1.calcular_perimetro()}")
