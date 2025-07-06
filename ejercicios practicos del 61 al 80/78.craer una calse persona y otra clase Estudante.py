"""78.craer una calse persona y otra clase Estudante
La clase Persona tiene el atributo
nombre y el metodo mostrar_nombre().
La clase Estudiante debe heredar la clase
Persona y utilizar el metodo mostrar_nombre()
de la clase Persona."""


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


class Estudiante(Persona):  # esta es la herencia.

    def __init__(self, nombre):
        super().__init__(nombre)

    def mostrar(self):
        super().mostrar_nombre()


Estudiante1 = Estudiante("jose")
Estudiante1.mostrar_nombre()
