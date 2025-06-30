"""77.crear una clase llamada persona.con atributus nombre , edad
*Un constructor, donde los datos pueden estar vacios.
*Los setters y getters para cada uno de los atributos.
*mostrar(): Muestra los datos de la persona.
*Esmayordeedad(): Devuelve un valor logico
indicando si es mayor de edad."""

class Persona:

    def __init__(self, nombre=None, edad=None):#para valor opcionales o vacios
        self._nombre = nombre  #el (_)es un modificador de acceso
        self._edad = edad

    @property
    def nombre(self): #va ser nuestro getter(parte del constructor)
        return self._nombre

    @nombre.setter   #setter(parte del constructor)
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self): #va ser nuestro getter
        return self._edad

    @edad.setter   #setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)#hacemos un diccionario

    def mayor_edad(self):
        if self._edad >= 18:
            return True
        else:
            return False

persona1 = Persona("jose", 25)
print("es mayor de edad", persona1.mayor_edad())
persona1.mostrar()
