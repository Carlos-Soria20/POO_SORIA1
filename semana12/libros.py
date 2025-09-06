# Sistema de Gestión de Biblioteca
# Este programa implementa un sistema básico para administrar una biblioteca,
# incluyendo libros, usuarios y operaciones de préstamo/devolución.

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un nuevo libro con sus datos básicos.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            categoria (str): Categoría o género del libro
            isbn (str): Número ISBN único del libro
        """
        self.datos_basicos = (titulo, autor)  # Tupla para garantizar inmutabilidad del título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """
        Retorna una representación en texto del libro.

        Returns:
            str: Descripción del libro
        """
        return f"'{self.datos_basicos[0]}' por {self.datos_basicos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un nuevo usuario de la biblioteca.

        Args:
            nombre (str): Nombre del usuario
            id_usuario (str): Identificador único del usuario
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros actualmente prestados por el usuario

    def __str__(self):
        """
        Retorna una representación en texto del usuario.

        Returns:
            str: Descripción del usuario y sus libros prestados
        """
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}, Libros Prestados: {[libro.datos_basicos[0] for libro in self.libros_prestados]})"


# Clase principal que administra la biblioteca
class Biblioteca:
    def __init__(self):
        """
        Inicializa una nueva biblioteca con colecciones vacías.
        """
        self.libros_disponibles = {}  # Diccionario: ISBN como clave, objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario: ID como clave, objeto Usuario como valor


    def añadir_libro(self, libro):
        """
        Añade un libro nuevo a la biblioteca.

        Args:
            libro (Libro): Objeto libro a añadir
        """
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está registrado.")


    def quitar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca por su ISBN.

        Args:
            isbn (str): ISBN del libro a eliminar
        """
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")


    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Args:
            usuario (Usuario): Objeto usuario a registrar
        """
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")


    def dar_baja_usuario(self, id_usuario):
        """
        Elimina un usuario de la biblioteca.

        Args:
            id_usuario (str): ID del usuario a eliminar
        """
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado del sistema.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")


    def prestar_libro(self, isbn, usuario):
        """
        Presta un libro a un usuario.

        Args:
            isbn (str): ISBN del libro a prestar
            usuario (Usuario): Usuario que solicita el préstamo
        """
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print(f"El libro con ISBN {isbn} no está disponible.")


    def devolver_libro(self, isbn, usuario):
        """
        Registra la devolución de un libro por parte de un usuario.

        Args:
            isbn (str): ISBN del libro a devolver
            usuario (Usuario): Usuario que devuelve el libro
        """
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print(f"El usuario {usuario.nombre} no tiene ningún libro con ISBN {isbn}.")


    def buscar_libros(self, criterio, valor):
        """
        Busca libros según un criterio específico.

        Args:
            criterio (str): Campo por el que buscar ('categoria', 'datos_basicos', etc.)
            valor (str): Valor a buscar
        """
        resultados = []

        for libro in self.libros_disponibles.values():
            if criterio == 'titulo' and libro.datos_basicos[0].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == 'autor' and libro.datos_basicos[1].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == 'categoria' and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio}: {valor}.")


    def listar_libros_prestados(self, usuario):
        """
        Muestra todos los libros prestados a un usuario específico.

        Args:
            usuario (Usuario): Usuario del que se listarán los libros
        """
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados actualmente.")


# Demostración del sistema
if __name__ == "__main__":
    # Instanciar objetos de las clases Libro, Usuario y Biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "9788437604947")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "9788498381492")
    usuario1 = Usuario("Jairo", "USR001")
    usuario2 = Usuario("Andrea", "USR002")
    biblioteca = Biblioteca()

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios en la biblioteca
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar un libro a un usuario
    biblioteca.prestar_libro("9788437604947", usuario1)

    # Mostrar libros prestados al usuario
    biblioteca.listar_libros_prestados(usuario1)

    # Devolver el libro prestado
    biblioteca.devolver_libro("9788437604947", usuario1)

    # Buscar libros en la biblioteca
    biblioteca.buscar_libros("categoria", "Infantil")

    # Mostrar el estado final del sistema
    print("\nEstado final:")
    print(f"Libros disponibles en la biblioteca: {len(biblioteca.libros_disponibles)}")
    for libro in biblioteca.libros_disponibles.values():
        print(f"- {libro}")

    print(f"Usuarios registrados: {len(biblioteca.usuarios_registrados)}")
    for usuario in biblioteca.usuarios_registrados.values():
        print(f"- {usuario}")