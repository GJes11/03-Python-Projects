
class Calculadora():

#Clase Aritmetica para realizar las operaciones de sumar, restar, etc

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
calculo = Calculadora(10, 5)
print(f'Suma: {calculo.sumar()}')
print(f'Resta: {calculo.restar()}')
print(f'Multiplicacion: {calculo.multiplicar()}')
print(f'Division: {calculo.dividir()}')