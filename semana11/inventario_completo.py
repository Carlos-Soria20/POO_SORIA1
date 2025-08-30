import json  # Aquí importo el módulo json para poder guardar y leer datos en formato JSON.

class Producto:  # Aquí defino la clase Producto q
    def __init__(self, id_producto, nombre, cantidad, precio):  # Aquí creo el constructor con los atributos necesarios.
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):  # Aquí creo un metodo para convertir el producto en un diccionario.
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def actualizar(self, cantidad=None, precio=None):  # Aquí creo un metodo para actualizar cantidad o precio.
        if cantidad is not None:  # Aquí verifico si se proporcionó una nueva cantidad.
            self.cantidad = cantidad  # Aquí actualizo la cantidad.
        if precio is not None:  # Aquí verifico si se proporcionó un nuevo precio.
            self.precio = precio  # Aquí actualizo el precio.

class Inventario:  # Aquí defino la clase Inventario que gestiona todos los productos.
    def __init__(self, archivo="inventario.json"):  # Aquí inicializo el inventario
        self.productos = {}  # Aquí creo un diccionario para guardar los productos con su ID como clave.
        self.archivo = archivo  # Aquí guardo el nombre del archivo JSON.
        self.cargar()  # Aquí llamo al metodo cargar para llenar el inventario desde el archivo.

    def cargar(self):  # Aquí defino el metodo para cargar los datos desde el archivo JSON.
        try:  # Aquí intento abrir el archivo y leer su contenido.
            with open(self.archivo, "r") as f:  # Aquí abro el archivo en modo lectura.
                datos = json.load(f)  # Aquí leo los datos en formato JSON.
                for item in datos:  # Aquí recorro cada producto en la lista.
                    prod = Producto(  # Aquí creo un objeto Producto con los datos del archivo.
                        item["id"],
                        item["nombre"],
                        item["cantidad"],
                        item["precio"]
                    )
                    self.productos[prod.id] = prod  # Aquí guardo el producto en el diccionario usando su ID.
        except FileNotFoundError:  # Aquí manejo el caso en que el archivo no exista.
            print("Archivo no encontrado. Se creará uno nuevo.")  # Aquí informo que se creará un nuevo archivo.
        except Exception as e:  # Aquí manejo cualquier otro error.
            print(f"Error al cargar: {e}")  # Aquí muestro el mensaje de error.

    def guardar(self):  # Aquí defino el metodo para guardar
        try:
            datos = [p.to_dict() for p in self.productos.values()]  # Aquí convierto cada producto en diccionario.
            with open(self.archivo, "w") as f:  # Aquí abro el archivo en modo escritura.
                json.dump(datos, f, indent=4)
        except Exception as e:  # Aquí manejo errores al guardar.
            print(f"Error al guardar: {e}")  # Aquí muestro el mensaje de error.

    def añadir(self, producto):  # Aquí defino el metodo para añadir un nuevo producto.
        if producto.id in self.productos:  # Aquí verifico si el ID ya existe en el inventario.
            print("Error: El ID ya existe.")  # Aquí informo que no se puede duplicar el ID.
        else:
            self.productos[producto.id] = producto  # Aquí añado el producto al diccionario.
            self.guardar()  # Aquí guardo los cambios en el archivo.
            print("Producto añadido.")  # Aquí informo que se añadió correctamente.

    def eliminar(self, id_producto):  # Aquí defino el metodo para eliminar un producto por su ID.
        if id_producto in self.productos:  # Aquí verifico si el producto existe.
            del self.productos[id_producto]  # Aquí elimino el producto del diccionario.
            self.guardar()  # Aquí guardo los cambios en el archivo.
            print("Producto eliminado.")  # Aquí informo que se eliminó correctamente.
        else:
            print("Producto no encontrado.")  # Aquí informo que no se encontró el producto.

    def actualizar(self, id_producto, cantidad=None, precio=None):  # Aquí defino el metodo para actualizar un producto.
        if id_producto in self.productos:  # Aquí verifico si el producto existe.
            self.productos[id_producto].actualizar(cantidad, precio)  # Aquí llamo al metodo actualizar del producto.
            self.guardar()  # Aquí guardo los cambios en el archivo.
            print("Producto actualizado.")  # Aquí informo que se actualizó correctamente.
        else:
            print("Producto no encontrado.")  # Aquí informo que no se encontró el producto.

    def buscar(self, nombre):  # Aquí defino el metodo para buscar productos por nombre.
        resultados = [  # Aquí creo una lista de productos que coincidan con el nombre.
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()  # Aquí comparo ignorando mayúsculas.
        ]
        return resultados  # Aquí devuelvo la lista de resultados.

    def mostrar_todos(self):  # Aquí defino el metodo para mostrar todos los productos.
        if not self.productos:  # Aquí verifico si el inventario está vacío.
            print("Inventario vacío.")  # Aquí informo que no hay productos.
        else:  # Si hay productos...
            print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10}")  # Aquí imprimo los encabezados.
            print("-" * 50)  # Aquí imprimo una línea separadora.
            for p in self.productos.values():  # Aquí recorro todos los productos.
                print(f"{p.id:<10} {p.nombre:<20} {p.cantidad:<10} ${p.precio:<10.2f}")  # Aquí imprimo los datos.

def menu():  # Aquí defino la función principal del menú.
    inventario = Inventario()  # Aquí creo una instancia del inventario.

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")  # Aquí pido al usuario que elija una opción.

        if opcion == "1":  # Si elige añadir producto...
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir(producto)

        elif opcion == "2":  # Si elige eliminar producto...
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar(id_producto)

        elif opcion == "3":  # Si elige actualizar producto...
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para mantener): ")
            precio = input("Nuevo precio (Enter para mantener): ")
            cantidad = int(cantidad) if cantidad.strip() else None
            precio = float(precio) if precio.strip() else None
            inventario.actualizar(id_producto, cantidad, precio)

        elif opcion == "4":  # Aquí gestiono la opción de buscar producto.
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar(nombre)
            if resultados:
                print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10}")
                print("-" * 50)
                for p in resultados:
                    print(f"{p.id:<10} {p.nombre:<20} {p.cantidad:<10} ${p.precio:<10.2f}")
            else:
                print("No se encontraron productos.")

        elif opcion == "5":  # Aquí gestiono la opción de mostrar todos los productos.
            inventario.mostrar_todos()

        elif opcion == "6":  # Aquí gestiono la salida del programa.
            print("¡Hasta luego!")
            break  # Aquí salgo del bucle y finalizo el programa.

        else:
            print("Opción inválida.")  # Aquí informo que la opción no es válida.

        # Aquí ejecuto el menú si el archivo se ejecuta directamente.
if __name__ == "__main__":
    menu()