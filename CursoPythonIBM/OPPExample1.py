"""
Definir una clase padre llamada Vehivulo y 2 clases hijas llamadas Coche y Bicicleta, las cuales heredan
de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos.

Vehiculo(Clase padre):
-Atributos (color, ruedas)
-Metodos (__init__ y __str__)

Coche(clase hija de vehiculo) (Ademas de los atributos y metodos heredados de Vehiculo)
-Atributo (velocidad (km/h))
-Metodos (__init__ y __str__)

Bicicleta(Clase Hija de Vehiculo) (Ademas de los atributos y metodos heredados de Vehiculo)
-Atributos( tipo(urbana/montaña/etc))
_Metodos(__init__ y __str__) 
"""

class Vehicle:
    def __init__(self, colour, wheels):
        self.colour = colour
        self.wheels = wheels
    
    def __str__(self):
        return 'Colour ' + self.colour + ', Wheels: ' + str(self.wheels)
    
class Car(Vehicle):
    def __init__(self, colour, wheels, speed):
        super().__init__(colour, wheels)
        self.speed = speed

    def __str__(self):
        return super().__str__() + 'Speed (km/h): ' + str(self.speed)

class Bicycle(Vehicle):
    def __init__(self, colour, wheels, type):
        super().__init__(colour, wheels)
        self.type = type
    def __str__(self):
        return super().__str__() + ', Type: ' + str(self.type)

#Crear un objeto de la clase vehiculo
vehicle = Vehicle('Red', 4)
print(vehicle)

#Crear un objeto de la clase hija coche
car = Car('Blue', 4, 150)
print(car)

#Crear un objeto de la clase hija bicicleta
bicycle = Bicycle('White', 2, 'MTB')
print(bicycle)
