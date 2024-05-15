
# POO

# Crear una CLASE

class Coche():
    #Declaracion de Atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_inMarcha = False

    #Declaracion de Metodos
    def arrancar(self):              # self hace referencia a la instancia de clase.
        self.is_inMarcha = True      # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_inMarcha == True):
            return "El coche esta arrancado"
        else:
            return "El coche esta parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche1 = Coche()
miCoche2 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
print("El largo del coche 1 es: ", miCoche1.largo, "cm")

miCoche1.arrancar()
print(miCoche1.estado())

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche 2 esta arrancado: ", miCoche2.arrancar())

#Modificamos el valor de una propiedad
miCoche2.ruedas = 10
print("El coche 2 tiene: ", miCoche2.ruedas, "ruedas")


# CREACIÓN DE UNA CLASE
class Usuario():
    nombre= "Angel"
    __edad= 47
    login= "admin"
    password= "1234"
    email= "angel@loquesea.com"
    telefono= 6767676767

 # Declaración de métodos
    def resumen(self):  # self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son: \n'
              f'Nombre: {self.nombre} \n'
              f'Edad: {self.__edad} \n'
              f'Login: {self.login}\n'
              f'Password: {self.password} \n'
              f'Email: {self.email}\n'
              f'Telefono: {self.telefono}')
    
    def cambia_edad(self):
        edadIntroducida = int(input('Introduzca edad (De 18-100): '))
        if 18<edadIntroducida<100:
            self.__edad = edadIntroducida
            print("Edad introducida correcta")
            return ""
        
    def muestra_edad(self):
        print("Edad introducida: ", self.__edad, "años")
        return ""

administrador = Usuario()
administrador.resumen()

print(administrador.cambia_edad())
print(administrador.muestra_edad())

#Creacion de una CLASE

class Moto():
    largo = 230
    ancho = 100
    ruedas = 2
    peso = 800
    cc = "1000"
    color = "verde"
    is_enMarcha = False
    velocidad_marcha = 0
    velocidad_marcha1 = 5

    def arrancar(self):             # self hace referencia a la instancia de clase.
        self.is_enMarcha = True     # Es como si pusiésemos mimoche.is_enMarcha = True
    
    def estado(self):
        if (self.is_enMarcha == True):  
            return "La moto esta arrancada"
        else:
            return "La moto esta apagada"
        
    def Subir_marcha(self):
        for i in range (1, 6):
            self.velocidad_marcha += 1
            print (f'La marcha actual es {self.velocidad_marcha}')
    
    def Bajar_marcha(self):
        for i in range (5, 0, -1):
            self.velocidad_marcha1 -=1
            print(f'La marcha actual es: {self.velocidad_marcha1}')

mi_Moto = Moto()

# Acceso a un atributo de la clase moto. Nomenclatura del punto.
print('La moto tiene:', mi_Moto.cc, 'centimetros cubicos')


mi_Moto.arrancar()
print(mi_Moto.estado())
print(mi_Moto.Subir_marcha())
print(mi_Moto.Bajar_marcha())
# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("La moto esta arrancada", mi_Moto.arrancar())