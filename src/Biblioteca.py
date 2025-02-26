from src.Libro import Libro


class Biblioteca:

    def __init__(self):
       self.list=[]


    def agregarLibros(self,libro):
      self.list.append(libro)


    def mostrarLibros(self):
        for num in self.list:
            print(f"{num.getTitulo()} : {num.getAnio()} : {num.getAutor()}")


    def buscar_por_autor(self,libroAutor):
        for elem in self.list:  # array de objetos
            if elem.getAutor() == libroAutor:
               return f"{elem.getAutor()} : {elem.getTitulo()}  : {elem.getAnio()}"
            else:
                return "No existe el autor"

biblioteca = Biblioteca()
libro1 = Libro("Romeo y Julia", "leonardo", 1965)
libro2 = Libro("Selena", "Cris", 1995)
libro3 = Libro("Corazon Principe", "Gracy", 2013)
libro4 = Libro("Diario de Anna", "Anna", 1945)
libro5 = Libro("Cometas en el cielo", "khaled", 1980)

print("agregando libros ...........")
biblioteca.agregarLibros(libro1)
biblioteca.agregarLibros(libro2)
biblioteca.agregarLibros(libro3)
biblioteca.agregarLibros(libro4)
biblioteca.agregarLibros(libro5)

biblioteca.mostrarLibros()

print(f"buscar libro por autor")
print(biblioteca.buscar_por_autor("leonardo"))




