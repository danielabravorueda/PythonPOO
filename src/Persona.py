
class Persona:

#Sin Constructor

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def saludar(self):
        return f"Hola mi nombre es {self.getNombre()} {self.getApellido()}"
