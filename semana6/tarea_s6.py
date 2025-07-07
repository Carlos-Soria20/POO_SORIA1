#Vamos a sacar el area de las figuras
import math  #Importamos la libreria math

# Creamos la clase padre que se llamara forma
class Forma:
    def area(self):  #Creamos un metodo
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Creamos la clase hija que va a heredar los metodos de la clase padre
class Circulo(Forma):
    def __init__(self, radio):  #creamos el constructor con el atributo radio
        self.__radio = radio #Encapsulamos radio


#Creamos los metodo get y set para el atributo que encapsulamos
    def get_radio (self):
        return  self.__radio

    def set_radio(self,radio):
        self.__radio = radio

    def area(self): #Definimos el metodo area
        return math.pi * (self.__radio ** 2)  # Área del círculo

    def mostrar(self):  #Vamos a mostrar el atributo encapsulado
        return f"El radio del circulo es {self.__radio}"

# Clase hija
class Rectangulo(Forma):
    def __init__(self, ancho, alto):  #Definimos el constructor y colocamos los atributos
        self.ancho = ancho
        self.alto = alto

    def area(self):  #Definimos el metodo area el cual es el mismo metodo pero realiza operaciones distintas
        return self.ancho * self.alto  # Área del rectángulo


# Crear instancias de las clases
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

#Imprimimos la instancia

print(f"El area del circulo es: {circulo.area()}")
print(f"El area del rectanfulo es: {rectangulo.area()}")

print(circulo.mostrar()) #Mostramos el metodo encapsulado
