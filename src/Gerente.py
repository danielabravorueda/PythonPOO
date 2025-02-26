from src.Empleado import Empleado

#clase HIJA
class Gerente(Empleado):

    def __init__(self,nombre,salario,departamento):
        super().__init__(nombre,salario)
        self.departamento = departamento

    def mostrar_info(self):
        return f"{self.nombre} : {self.salario}  : {self.departamento}"

gerente = Gerente("Gerente",5000,"IT")
print(gerente.mostrar_info())

