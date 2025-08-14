class Producto:  #Creamos nuestra clase producto
    def __init__(self, id_producto, nombre, cantidad, precio):  #Creamos nuestro constructor y agregamos los atriubutos que se va a inicializar
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):  #Definimos el metodo get para visualizar
        return self.id_producto

    def get_nombre(self): #Definimos el metodo get para visualizar
        return self.nombre

    def get_cantidad(self): #Definimos el metodo get para visualizar
        return self.cantidad

    def get_precio(self): #Definimos el metodo get para visualizar
        return self.precio

    def set_cantidad(self, cantidad): #Creamos el metodo set
        self.cantidad = cantidad

    def set_precio(self, precio): #Creamos el metodo set
        self.precio = precio

#Creamos nuestra clase de inventario
class Inventario:
    def __init__(self):
        self.productos = []  #Creamos una lista vacia para luego agregar los productos
    #Creamos un metodo para añadir el producto
    def añadir_producto(self, producto):
         for p in self.productos:  #Con un for vamos a iterar sobre la lista de productos
            if p.get_id() == producto.get_id():  #Con una condicional si el id del prodcuto es igual al prodcuto que ingresamos
                print("Error: El ID ya existe.")  #Vamos a colocafr un print con un mensaje que ya existe el producto
                return
         self.productos.append(producto)  # Sino entra al if, agregaremos a nuestra lista de prodcutos el nuevo prodcuto ingresado
         print("Producto añadido exitosamente.")  #Mostramos un mensaje

    #Creamos un metodo para eliminar el producto
    def eliminar_producto(self, id_producto):
        # Eliminar el producto si el ID coincide
        for p in self.productos:  #Iteramos sobre nuestra lista de productos
            if p.get_id() == id_producto:
                self.productos.remove(p)  #Eliminamos el producto con remove
                print("Producto eliminado exitosamente.")  #Enviamos un mensaje de que se elimino el prodcuto exitosamente
                return
        print("Error: Producto no encontrado.")  #Nos aseguramos con un mensaje que si no hay, no se encontro el producto


    #Ahora cremoas un metodo para actualizar
    def actualizar_producto(self, id_producto, cantidad=None, precio=None): #Creamos el constructor y colocamos atriubutos que sean igual a none
        for p in self.productos:  #Iteramos sobre la lista
            if p.get_id() == id_producto:
                if cantidad is not None:  #Si la cantidad no es none
                    p.set_cantidad(cantidad)  #Llamamos al metodo set y podemos actualizar la nueva cantidad proporcionada
                if precio is not None: #Si la cantidad no es none
                    p.set_precio(precio) #Establece el precio del producto al nuevo precio proporcionado
                print("Producto actualizado exitosamente.")  #Enviamos un mensaje que el producto fue exitosamente actualizado
                return
        print("Error: Producto no encontrado.")

    #Cremos un metodo para buscar el producto

    def buscar_producto(self, nombre):
        resultados = [] #Los resultados vamos a guardar en una lista
        for p in self.productos:  #Iteramos sobre los productos
            if nombre.lower() in p.get_nombre().lower():  #Verifcamos si el nombre en minuscula esta contenido en el nombre del producto
                resultados.append(p)  #Si se cumple el  producto p se añade a la lista resultados.
        return resultados # retornamos la lista resultados que contiene todos los productos

    #Creamos un metodo para mostrar los productos
    def mostrar_productos(self):
        if len(self.productos) == 0:  #Si la longitud de prodcutos en igual a cero
            print("No hay productos en el inventario.") #Enviamos un mensake que no existe prodcutos
        else: #Sino
            for p in self.productos: #Iteramos la lista de prodcutos
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")  #Imprimimos los prodcutos con los atributos

#Creamos una funcion para el menu
def menu():
        inventario = Inventario()
        while True:  #Creamos un bucle while y colocamos opciones
            print("\n--- Menú de Gestión de Inventarios ---")
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Mostrar todos los productos")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")


            if opcion == '1': #Si la ocpion es añadir
                id_producto = input("Ingrese ID del producto: ")  #Pedimos el id
                nombre = input("Ingrese nombre del producto: ") #Pedimos el nombre
                cantidad = int(input("Ingrese cantidad: "))  #Ingrese la cantidad
                precio = float(input("Ingrese precio: "))  #Pedimos el precio
                producto = Producto(id_producto, nombre, cantidad, precio)   #Nos muestra el prodcuto
                inventario.añadir_producto(producto)

            elif opcion == '2':  #Si elije eliminar
                id_producto = input("Ingrese ID del producto a eliminar: ")  #Pedimos el id del producto
                inventario.eliminar_producto(id_producto)  #Eliminamos

            elif opcion == '3': #Si elije actualizar
                id_producto = input("Ingrese ID del producto a actualizar: ")  #Pedimos el id del prodcuto
                cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiar): ")  #Colocamos la cantidad
                precio = input("Ingrese nuevo precio (deje en blanco si no desea cambiar): ")  # Podemos actualizar el precio
                inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                               float(precio) if precio else None)

            elif opcion == '4':  #Si la opcion es buscar
                nombre = input("Ingrese nombre del producto a buscar: ")  #Colcoamos una variable para buscar el producto
                resultados = inventario.buscar_producto(nombre)
                if resultados:  #Si resultados es verdadero
                    for p in resultados:  #Iteramos sobre los reusltados
                        print(
                            f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")  #Imprimimos la busqueda
                else:
                    print("No se encontraron productos.")  #Sino, colocamos un mensaje que no se econtro el producto

            elif opcion == '5':  #Si la opcion es mostrar los prodcutos
                inventario.mostrar_productos()  #llamamos al metodo buscar

            elif opcion == '6':  #Si elejimos 6
                print("Saliendo del sistema.") #Imprimimos un mensaje de saliendo
                break  #Cortamos el programa queda hasta ahi

            else:
                print("Opción no válida. Intente de nuevo.")  #Si eleije otra ocpion va a dar error de opcion no valida

#Llamamos a la funcion menu
if __name__ == "__main__":
    menu()