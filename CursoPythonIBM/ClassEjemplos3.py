#EL BUCLE FOR

# Ejecuta el print dos veces
for i in [1,10]:
      print("Hola")

# Imprime el contenido del diccionario
for i in ["primavera", "verano", "otoño", "invierno"]:
      print(i)  # Repite el print tantas veces como caracteres hay en el string 

# recorre cada letra de "frase" e imprime hola cada vez; end=" " para que imprima todo en la misma linea
for i in "frase":
      print("hola", end=" ")

# Evaluamos si un mail contiene el caracter @
miemail = input("Introduce email: ")
email = False
for i in miemail: 
    if i == "@":
        email = True
if email == True:   #Se puede simplificar    if email:
    print("El email es correcto")
else: 
    print("El email es incorrecto")

# Podemos unir valores de texto con valores de variable a la hora de imprimir:
for i in range(5):
    print(f"Valor de la variable {i}")
for i in range(5, 10):
    print(f"Valor de la variable {i}")  # f-string puedes incluir expresiones dentro de llaves {} dentro de la cadena, 
#y estas expresiones serán evaluadas y su resultado será insertado en la cadena en esa posición

# Podemos poner un tercer argumento con el que especificamos de cuanto en cuanto va el conteo:
for i in range(5, 10, 2):
    print(f"Valor de la variable {i}")

# Validar un mail en función de si tiene @ simplemente recorriendo la logitud del string:
Valido = False
email = input("Introduzca email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

# Las cadenas son objetos iterables, contienen una secuencia de caracteres:
for x in "Banana":
    print(x)

# Con la instrucción break podemos detener el ciclo antes de que haya pasado por todos los elementos:
# Salga del bucle cuando x es "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break 

# Salga del bucle cuando x es "banana", pero esta vez el corte se produce antes de la impresión:
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        break
    print(x)

# Con la instrucción continue podemos detener la iteración actual del ciclo y continuar con la siguiente:
# En este caso no me imprimiría "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        continue
    print(x)
    
# Para recorrer un conjunto de código un número específico de veces, podemos usar la función range ()
for x in range(6):
      print(x)

# Función range con parámetro de inicio incrementado por defecto en 1.
for x in range(2, 6):
      print(x)

# Función range con parámetro de inicio incrementado en 3.
for x in range(2, 20, 3):
      print(x)

# BUCLE FOR ANIDADO
# Imprime cada color para cada fruta:
color = ["roja", "amarilla", "verde"]
frutas = ["manzana", "banana", "cereza"]

for x in frutas:
    for y in color:
        print(x, y)

# Los bucles for no pueden estar vacíos. 
# Si por alguna razón tenemos un bucle for sin contenido, usaremos la instrucción pass para evitar un error.

for x in [0, 1, 2]:  
  pass

# BUCLE WHILE
# WHILE

# Imprime edad cuando el contador llegue a 18
edad = 0
while edad <18:
      edad = edad +1
print("Tienes" + str(edad))

# Pregunta la edad mientras sea negativa
edad = int(input("Introduzca edad: "))


edad=int(input("Introduce edad: "))
while edad < 0:
      print("Edad incorrecta")
      edad = int(input("Introduzca edad: "))
print("Tu edad es: " + str(edad))

# Calcula la raiz cuadrada de un número. Tenemos tres intentos y el número no puede ser negativo.
import math;
intentos = 0;
num = int(input("Introduzca número: "))
while num < 0:
    print("Incorrecto")
    num=int(input("Introduce numero: "))

    if intentos ==2:
          print("Demasiados intentos")
          break;
if intentos <2:
      intentos = intentos +1
      solucion = math.sqrt(num)
      print("La raiz cuadrada de " + str(num) + "es:" + str(solucion))
   

# Bucle while con un if anidado y un break
# Salga del bucle cuando num sea 3:
num4 = 1
while num4 <6: 
    print(num4)
    if num4 ==3:
        break
    num4 +=1

#LISTAS
"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""
miLista = ["Angel", 43, 6859385, "Alvaro"]
miLista2 = [22, True, "Hola", [1, 2, "Adios"]]

# MÉTODOS DE LAS LISTAS
# Hacer una lista de una cadena
miLista3 = list("PYTHON")
print(miLista3)

# Acceder a los elementos de una lista
miLista4 = [22, True, "una cadena", [1, 2]]
print(miLista4[1])

miLista5 = [[1,2] , [3,4] , [5,6]]
miVar = miLista5[1][2]
print(miVar)

# Función con una lista como parámetro

def miFuncion(listaFrutas): #Definicion de la funcion
      for x in listaFrutas: #Iteracion a traves de la lista
        print(x)

frutas = ["Manzana", "Pera", "Banana"]  #Creamos una lista 

miFuncion(frutas)   #Llamamos a la funcion pasando la lista como argumento

# TUPLAS

#Una tupla es una colección ordenada e inmutable. En Python, las tuplas se escriben entre paréntesis.

# Declaración de una tupla

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

# Otra forma de declararla
miTupla1 = tuple(("mnanzana", "banana", "cereza"))
print(miTupla1)

# Indexación Negativa
miTupla2 = ("manzana", "banana", "cereza")
print(miTupla2[-1])

# Rango de índices. Devuelve el tercer, cuarto y quinto elemento:
miTupla3 = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla3[2:5])

# Convierta la tupla en una lista para poder cambiarla:
miTupla4 = ("manzana", "banana", "cereza")
miLista1 = list(miTupla4)
miLista1[1] = "kiwi"
miTupla4 = tuple(miLista1)

print(miTupla4)

# Recorrer una tupla
miTupla5 = ("manzana", "banana", "cereza")
for x in miTupla5: 
    print(x)


# Comprobar si existe un elemento. Compruebe si "manzana" está presente en la tupla:
miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
    print("Si, esta en la tupla")

print("manzana" in miTupla)     # Otra forma, simplemente con un boolean

# Longitud de la tupla
miTupla6 = ("manzana", "banana", "cereza")
print(len(miTupla6))

# Unir dos tuplas
tupla1 = ("a", "b", "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

# Cuantas veces se encuentra el elemento 4 en miTupla?
miTupla7 = ("manzana", "banana", "cereza" , "manzana")
print(miTupla7.count("manzana"))

# Desempaquetado de tupla
miTupla8=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3,=miTupla8

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)


# DICCIONARIOS

"""Los diccionarios, también llamados matrices asociativas, deben su nombre a que son 
colecciones que relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. 
En Python, los diccionarios se escriben entre llaves y tienen claves y valores.
"""

# Declaración de un diccionario
miDiccionario = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964 
}
print(miDiccionario)

# A los valores almacenados en un diccionario se accede por su clave

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

peliculas["Amélie"]

# Reasignar valores a un diccionario
peliculas ["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

# Usar una tupla dentro de un diccionario:
miDiccionario2 = {"nombre": "Jordan", "Equipo": "Bulls", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario2["anillos"])

# Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}

peliculas.pop("Love Actually")
print(peliculas)

# Crear un diccionario a partir de dos listas:
lista_valores = ["Angel", 43]
lista_claves = ["Nombre", "Edad"]
diccionario = dict(zip(lista_claves, lista_valores))
print(diccionario)

# Para comprobar si una clave está en el diccionario:
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
"nombre" in diccionario		#Devuelve true o false

# Imprima las claves del diccionario:
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
for x in peliculas:
    print(peliculas[x])

# Longitud de un diccionario:
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
print(len(peliculas))

# Agregar elementos a un diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}

miDiccionario["color"] = "red"
print(miDiccionario)

# Eliminar el último elemento insertado:

miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario.popitem()
print(miDiccionario)

# La palabra clave del elimina el elemento con el nombre de clave especificado:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
del miDiccionario["year"]
print(miDiccionario)

# La palabra clave del también puede eliminar completamente el diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
del miDiccionario
print(miDiccionario)

# La palabra clave clear() vacía el diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}

miDiccionario.clear()
print(miDiccionario)
      
# Copiar un diccionario
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
miDict1 = miDiccionario.copy()
print(miDict1)

# Otra forma de copiar un diccionario
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}

miDict2 = dict(miDiccionario)
print(miDict2)

# Diccionarios anidados
child1 = {"name":"Emily", "year": 2004}

child2 = {"name": "Tobias", "year": 2006}

child3 = {"name": "Hank", "year": 2000}

my_family = {"child1": child1, "child2":  child2, "child3": child3}

print(my_family["child2"])