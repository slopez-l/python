"""74.crear una clase persona con los siguientes atributos:
*** nombre, edad, dni
con elos metodos:
init()
es_mayor_de_edad()este retorna si es mayor de edad"""


class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True


persona1 = Persona("sergio", 20, "hey")

print("el nombre es ", persona1.nombre)

if persona1.es_mayor_de_edad():
    print("es mayor de edad")
