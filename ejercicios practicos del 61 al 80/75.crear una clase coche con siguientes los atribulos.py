"""75.crear una clase coche con los atribulos:
marca, modelo, matricula, km
con los metodos:
init como constructor
avanzar(km) este aumenta
el valos de km en la cantidad"""


class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km

    def avanzar(self, km):
        self.km = self.km + km


coche1 = Coche("ford", "fiesta", "12234hihh", 5000)
print(coche1.__dict__)
coche1.avanzar(3000)
print(coche1.__dict__)
