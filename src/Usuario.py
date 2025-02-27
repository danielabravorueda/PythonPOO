class Usuario:
    def __init__(self,nombre,correo):
        self.nombre = nombre
        self.correo = correo

    def iniciar_sesion(self,name,email):
        if self.nombre == name and self.correo == email:
            return "Ingresando ....."
        else:
            return "El correo no existe"

usuario = Usuario("dani","dbr@gmail.com")

print(usuario.iniciar_sesion("dani","dani@gmail.com"))