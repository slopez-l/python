"""76.crear una clase animal con los atributos
 especie y nombre.
 La clase debe tener los metodos:
 init y hablar
 el metodo ahbalar  nos retorna una palabra segun la
 interpretacion del sonido como un perro seria
 "guau."""


class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        if self.especie == "perro":
            print("Guau!")
        elif self.especie == "gato":
            print("Miau!")
        else:
            print(".....")


perro = Animal("perro", "bimba")
gato = Animal("gato", "Misa")

perro.hablar()
gato.hablar()

print(perro.__dict__)
