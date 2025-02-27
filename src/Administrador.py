from src.Usuario import Usuario


class Administrador(Usuario):
    def __init__(self,nombre,correo):
        super().__init__(nombre,correo)

    def eliminarUsuario(self,name):
        if name == self.nombre:
            return "Eliminando ....."
        else:
            return "Usuario no encontrado"

administrador = Administrador("mario","mari56@gmail.com")
print(administrador.eliminarUsuario("dani"))