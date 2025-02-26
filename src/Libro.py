class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo = titulo
        self.autor=autor
        self.anio=anio

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getAnio(self):
        return self.anio
