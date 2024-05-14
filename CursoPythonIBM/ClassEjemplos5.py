# FUNCIONES

# Definición de una función. Importante la identación:
def my_function():
    print("Estamos ejecutando la funcion")

# Llamada a la función. En otra parte de mi código, llamamos a la función para que se ejecute:
my_function()

#----------------------------------------------

def suma():
    num1 = 3
    num2 = 5
    print("suma = ", num1+num2)

suma()

# Otra opcion
def suma1():
    num1=6
    num2=5
    resultado=num1+num2
    return resultado

print(suma1())

#El bloque de código que ejecutará la función incluye todas las declaraciones con indentación 
# dentro de la función.
def my_function():
    print("this will print")
    print('so will this')

x=7
# la asignación de x no es parte de la función ya que no está indentada
#---------------------------------------

# Las variables definidas dentro de una función solo existen dentro del ámbito de esa función.
def duplica(num):
    x=num*2
    return x
#print(x)    #error x no esta definida
print(duplica(4))
#---------------------------------------

#Si la definición de una función incluye parámetros, debe proporcionar el mismo número 
# de parámetros cuando llame a la función.
def multiplica(arg1, arg2):
    return arg1*arg2
#print(multiplica(3))  # TypeError: multiplica() utiliza exactamente 2 argumentos (0 proporcionados)

print(multiplica('a',6))    #'aaaaaa' mostrado en consola

#print(multiplica('a', 'b'))  # TypeError: Python no puede multiplicar dos strings


#---------------------------------------
#Puedes pasar los parámetros en el orden que desees, utilizando el nombre del parámetro.
def suma(a,b):
    return a+b

result = suma(b=2, a=3)
print(result)   # result = 4

#---------------------------------------
#También podríamos pasar varios valores que retornar a return.
def f(x, y):
    return x *2, y *2
a, b =f(1, 2)

""" Sin embargo, esto no quiere decir que las funciones Python puedan de-volver varios valores, 
 lo que ocurre en realidad es que Python crea una tupla al vuelo cuyos elementos 
 son los valores a retornar, y esta única variable es la que se devuelve."""

#   -------------------------------------
# función con un parámetro
#   -------------------------------------

# Declaración de una función
def miFuncion(num1, num2):
    return (num1 + num2)

# Llamada a la función
print(miFuncion(2,3))

#   -------------------------------------
  # llamada a la función, 'Hola Angel!' se muestra en la consola
#   -------------------------------------
def hola_con_nombre(name):
    print('Hola ' + name + '!')

hola_con_nombre('Angel')    #llamada a la funcion. 'hola Angel! se muestra en la consola
#---------------------------------------

# Funcion con parametro por defecto
#---------------------------------------
def imprimir(precio, iva = 1.21):
    print(precio*iva)

imprimir(300, 1.08)
imprimir(300)   #para usar el valor de iva predeterminado en la funcion, no se pone valor

# Funciones con argumentos variables
# Me crea una tupla de nombre "otros" 
def varios(param1, param2, *otros):
    for val in otros:
        print(val)

varios(1,2)
varios(1,2,3)
varios(1,2,3,4)

"""
También se puede preceder el nombre del último parámetro con **, 
en cuyo caso en lugar de una tupla se utilizaría un diccionario. 
Las claves de este diccionario serían los nombres de los parámetros 
indicados al llamar a la función y los valores del diccionario, 
los valores asociados a estos parámetros.
"""
def varios(param1, param2, **otros):
    for i in otros.items():
        print(i)

varios(1, 2, tercero=3)

# ---------------------------
#---------------------------------------
#ARGUMENTOS VARIABLES EN FUNCIONES. EL ARGUMENTO CON * SERÁ UNA TUPLA
# PYTHON NO TIENE SOBRECARGA DE FUNCIONES
#---------------------------------------
def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listaNombres("Juan", "Laura", "Maria")
listaNombres('Juan', 'Pedro')

#---------------------------------------
# HACER LO MISMO PERO PASANDO DICCIONARIOS COMO ARGUMENTOS. KWARGS
def listarTerminos(**KWARGS):
    for clave, valor in KWARGS.items():
        print(f'{clave}: {valor}')

listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')
#---------------------------------------
def mi_funcion(nombre, apellido):
    print('saludos desde mi funcion')
    print(f'Nombre {nombre}, Apellido {apellido}' )

mi_funcion('Alberto', 'Garcia')
#---------------------------------------
# RETURN
#---------------------------------------

# Definiciones de funcion no pueden estar vacías, pero si por alguna razón tiene 
# una definición de funcion sin contenido, ingrese la instrucción pass para evitar un error.
def myFunction():
    pass
    
#---------------------------------------
def sumar(a, b):
    return a+ b

resultado = sumar(3, 5)
print(f'resultado sumar: {resultado}')


#También podíamos haber llamado a la función dentro de nuestro método print
print(f'Resultado sumar: {sumar(5,3)}')

# ---------------------------
# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2

multiplica(3, 5)    #Muestra 15 en la consola
#---------------------------------------

# esta es una función básica de suma
def suma(a, b):
    return a+b
result = suma(1, 2)
# result = 3
#---------------------------------------


# VALORES POR DEFECTO
#---------------------------------------
# esta es una función básica de suma con valores predeterminados
def suma(a, b=3):
    return 1+b
resultado = suma(1)
# result = 4
#---------------------------------------

# Indicio de qué tipo de dato vamos a manejar:
#---------------------------------------
def sumar(a:int = 0, b:int = 0) -> int:
#def sumar(a = 0, b = 0):
    return a + b
resultado = sumar()
#print(f'Resultado sumar: {resultado}')
print(f'Resultado suma: {suma(45, 654)}')
#uanque le hemos dicho el tipo de los parámetros no estamos obligados a cumplirlo.
print(f'Resultado sumar: {sumar("ANGEL", "Garcia")}')
#---------------------------------------
"""
Crear una función para sumar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función 
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""

# Definimos nuestra funcion para sumar valores
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado

# Llamada a la funcion
print(sumar_valores(3, 5, 9, 4, 6, 45, 444))
#---------------------------------------

# Distintos tipos de datos como argumentos en Python
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))
desplegarNombres([10,11])
#---------------------------------------

# FUNCIONES RECURSIVAS

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 6
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')

#---------------------------------------
"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

Si se pasan valores negativos no imprime nada
"""
#---------------------------------------

def imprimir_numero_recursivo(numero):
    if numero == 1:
        print(numero)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor incorrecto')

imprimir_numero_recursivo(10)
#--------------------------------------------------

def cuenta_regresiva(numero):
    numero==1
    if numero >0:
        print(numero)
        cuenta_regresiva(numero-1)
    else:
        print('BOOOOOO')
        print('Fin de la funcion'), numero

cuenta_regresiva(5)
#---------------------------------------
"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    return pago_total

# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
#---------------------------------------
#---------------------------------------

"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) *5 / 9

# Realizamos algunas pruebas de conversion
celsius = float(input('Introduzca valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')

# Realizamos la prueba de grados fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:0.2f}')



