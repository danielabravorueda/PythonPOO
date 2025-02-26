#CLASE PADRE
class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"{self.nombre} : {self.salario}"

empleado = Empleado("Empleado", 5000)
print(empleado.mostrar_info())

