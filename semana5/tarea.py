import math  #Importamos la libreria math

class Cuadrado:  #Creamos una clase llamada cuadrado
    def __init__(self, lado: float):   # Creamos el constructor y le asignamos un valor flotante
        self.lado = lado  # float: longitud del lado del cuadrado

    def calcular_area(self) -> float:   #Creamos un metodo para calcular el area
        return self.lado ** 2  # retornamos el área del cuadrado

class Circulo:  #Creamos una clase llamada circulo
    def __init__(self, radio: float):  #Creamos un constructor y declaramos atributos tipo flotante
        self.radio = radio  # f radio del círculo

    def calcular_area(self) -> float:  #Creamos un metodo para calcular el area del circulo
        return math.pi * (self.radio ** 2)  # área del círculo


# Solicitar al usuario el lado del cuadrado
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))  # float
cuadrado = Cuadrado(lado_cuadrado)  #Instanciamos el objeto cuadrado con nuestra clase Cuadrado
area_cuadrado = cuadrado.calcular_area()   #Llamamos al metodo calcular area
print(f"El área del cuadrado es: {area_cuadrado:.2f}")  #Imprimimos

# Solicitar al usuario el radio del círculo
radio_circulo = float(input("Ingrese el radio del círculo: "))  # float
circulo = Circulo(radio_circulo) #Creamos nuestra instancia
area_circulo = circulo.calcular_area() #Llamos al metodo calcular del circulo
print(f"El área del círculo es: {area_circulo:.2f}")  # Imprimimos