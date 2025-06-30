"""99.crear un programa que permita crear, leer y agregar
 informacion a in archivo txt"""

class Archivo:

    def __init__(self):
        self.nombre_archivo = ""
        self.contenido = ""

    def set_nombre_archivo(self, nombre):
        self.nombre_archivo = nombre

    def set_contenido(self, contenido):
        self.contenido = contenido

    def crear_archivo(self):
        with open(self.nombre_archivo, "w"):
            pass

    def escibir(self):
        with open(self.nombre_archivo, "w") as archivo:
            archivo.write(self.contenido)

    def leer_archivo(self):
        with open(self.nombre_archivo, "r") as archivo:
            informacion = archivo.read()
        return informacion

file = Archivo()
file.set_nombre_archivo("archivo.txt")
file.set_contenido("hola que tal autodidacta")
file.crear_archivo()
file.escibir()
print(file.leer_archivo())

