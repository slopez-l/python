"""79.representa una cuenta ancaria con deposito y retiro.
debe haber un titular y un saldo utiliza POO"""


class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("se deposito ", cantidad)

    def retirar(self, cantidad):
        self.saldo -= cantidad
        print("se teriro ", cantidad)

    def mostrar(self):
        print(self.__dict__)


cuenta1 = Cuenta("pepe", 500)
cuenta1.mostrar()
cuenta1.depositar(1000)
cuenta1.mostrar()
cuenta1.retirar(300)
cuenta1.mostrar()
