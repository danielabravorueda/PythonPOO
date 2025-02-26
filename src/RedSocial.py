from src.Persona import Persona


class RedSocial:

#Crear Instancias de Clases

    def __init__(self):
        self.persona1 = Persona()
        self.persona1.setNombre("Daniela")
        self.persona1.setApellido("Bravo")

        self.persona2 = Persona()
        self.persona2.setNombre("Roxi")
        self.persona2.setApellido("Delgadillo")

    def saludoPersona1(self):
        return f"{self.persona1.getNombre()} {self.persona1.getApellido()}"


    def saludoPersona2(self):
        return f"{self.persona2.getNombre()} {self.persona2.getApellido()}"


redSocial = RedSocial()
print(redSocial.saludoPersona1())
print(redSocial.saludoPersona2())