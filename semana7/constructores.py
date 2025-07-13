# Creamos una clase Libro que almacena el título y el autor
class Libro:
    def __init__(self, titulo, autor):  # Inicializamos los atributos
        self.titulo = titulo
        self.autor = autor
        print(f"Libro creado: '{self.titulo}' por {self.autor}")  # Mensaje al crear

    def mostrar(self):  # Método para presentar el libro
        print(f"Este libro se llama '{self.titulo}' y fue escrito por {self.autor}.")

    def __del__(self):  # Destructor que se llama al eliminar la instancia
        print(f"Libro eliminado: '{self.titulo}'")

# Creamos una instancia de Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Llamamos al método para mostrar información del libro
libro1.mostrar()

# Eliminamos la instancia para activar el destructor
del libro1