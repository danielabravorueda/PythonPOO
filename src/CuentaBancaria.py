from src.RedSocial import RedSocial


class CuentaBancaria:

    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self,saldo):
        self.saldo += saldo

    def retirar(self,saldo):
        self.saldo -= saldo

    def mostrarSaldo(self):
        return self.saldo

cuenta = CuentaBancaria("dani",200)
cuenta.depositar(100)
cuenta.retirar(20)
print(cuenta.mostrarSaldo())