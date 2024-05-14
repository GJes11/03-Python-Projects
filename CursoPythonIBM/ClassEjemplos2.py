#VARIBLES
#Variable numerica entera
n_age = 34

#Variable numerica float
n_receipt = 23.876

#Variable tipo string
s_name = 'Mark is my "only" friend'

#Variable String en varias lineas
s_longText = """This is a message
...with three line
... jumps"""

# Sobreescribimos el valor de la variable s_edad y ahora la ponemos como string:
s_age = "47"

# Declaración de constante:
PINUMBER = 3.14159

# Declaración de un boolean
is_single = True
is_married = False

# True = 1 y False = 0
True == 1
False ==0
print(True + 2)

# Cuando se valida una condición , Python devuelve True o False:
print(10 > 8)
print(10 == 9)
print(7 < 9)

# Declaración múltiple
# En una sola instrucción, estamos declarando tres variables: a, b y c, y asignándoles un valor concreto a cada una.
a, b, c = 'string', 15, True
# Sería como poner:
a = 'string'
b = 15
c = True

# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :
print(type(n_age))
print(type(n_receipt))
print(type(s_name))
print(type(PINUMBER))
print(type(is_single))

#CASTING
#Forzado de tipo enteros
x = int(1)      #x vale 1
y = int(2.8)    #y vale 2
z = int("3")    #z vale 3

#Forzado de tipo float
x = float(1)        #x vale 1.0
y = float(2.8)      #y vale 2.8
z = float("3")      #z vale 3.0
w = float("4.2")    #w vale 4.2

#Forzado de tipo string
x = str("s1")   #x vale's1'
y = str(2)      #y vale'2'
z = str(3.0)    #z vale'3.0'

#Casting. Reconversion de tipos
#De Int a Float
n_number = 13
n_number2 = float(n_number)

#De Float a Int
n_number3 = 24.987
n_number4 = int(n_number3)

#De String a Int
s_text = "12"
n_number5 = int(s_text)

#De Int a String
n_number6 = 25
s_text2 = str(n_number6)

print(n_number2)
print(type(n_number2))
print(n_number4)
print(type(n_number4))
print(n_number5)
print(type(n_number5))
print(s_text2)
print(type(s_text2))


#OPERADORES
#Módulo. Nos devuelve el resto de una división:
n_numerator = 85
n_denominator = 9
n_rest = n_numerator % n_denominator
print("The rest of the division" , n_numerator, "and" , n_denominator, "is" ,n_rest)

#==  Igual que... (No confundir con el operador de asignación =)
#Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.
n_number1 = 34
s_text1 = "34"
n_number1 == s_text1

n_number7 = 34
n_number8 = 34
n_number7 == n_number8

#!=  Diferente que...
n_number_1 = 30
n_number_2 = 31
n_number_1 != n_number_2

#+=  Suma e incremento
n_number_3 = 34
n_number_3 += 1 #Sería como poner: n_numero6 = n_numero6 +1 
print(n_number_3)


#METODOS STRING
#find() retorna la posición de la primera similitud de la substring
cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print(cadenaDeTexto.find('quien'))  #Devolvería: 52

#rfind() retorna la última posición de la similitud de la substring.
cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print(cadenaDeTexto.rfind('quien'))     #Devolvería: 94; Si, el substring no es encontrado retorna -1.

#replace() Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
miString = "Esto es bonito. Esto es bueno."
newString = miString.replace("es" ,"FUE")
print(newString)    #Devolvería: Esto FUE bonito. Esto FUE bueno.

#PRINT
#Salida de directa de datos
print("En esta ocasión hemos imprimido por pantalla este string")

#Salida de datos calculados
n_numero_4 = 4
n_numero_5 = 6
print("El resultado de sumar" , n_numero_4, "y" , n_numero_5 , "es" , (n_numero_4+n_numero_5))

#Si concatenamos int y strings usando el signo + nos puede dar problemas.
#print("El resultado de sumar " + n_numero_4 + " y " + n_numero_5 + " es " + (n_numero_4+n_numero_5))
#Sale este print:
#print("El resultado de sumar" + " " + " os numeros")

#INPUT
s_nombreIntroducido = input("Introduzca su nombre: ")
print("Bienvenido", s_nombreIntroducido)

"""   IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea un número, 
por lo que, si necesitamos operar matemáticamente con números, tendremos que hacer un casting: 
"""
s_edad = int(input("Introduzca su edad: "))
print("El año que viene tendrá usted ", s_edad + 1, "años")

#METODOS STRINGS
#TRABAJAR CON STRINGS
"""Los strings son secuencias de caracteres de texto. 
Todos los objetos en Python se engloban en dos categorías: mutables o inmutables. 
Los tipos básicos mutables son las listas, los diccionarios y los sets. 
Los tipos básicos inmutables son los números, los strings y las tuplas. 
Los objetos mutables pueden ser cambiados en el mismo objeto, mientras que los inmutables no.
"""
# Para concatenar textos se hace con “+” o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.
print("Esta frase" , "termina aquí")
print("Esta frase" + "termina aquí")

# Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b		 # c es "unodos"
c = b * 3 		 # c es "dosdosdos"

# MÉTODOS DE LOS STRINGS:

# lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower())

# capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize())

# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3.count('c'))

# find(): Representa el índice o la posición en el cual aparece un carácter o un grupo de caracteres. 
# Si aparece varias veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4.find('e'))

# rfind(): Igual que find() pero contando desde atrás.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5.rfind('desde'))

# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un string. 
# Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"
print(s_texto6.isdigit())

# isalum(): Devuelve un boolean, Devuelve verdadero si todos los caracteres de la cadena son numéricos 
# y hay al menos un carácter. En caso contrario, devuelve falso.
s_texto7 = "9857654gf7"
print(s_texto7.isalnum())

# isalpha(): Devuelve un boolean, comprueba si hay sólo letras. Los espacios no cuentan.
s_texto8 = "Holamundo"
print(s_texto8.isalpha())

# split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())

# Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print(s_texto10.split(","))
 
# strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = "   En este texto había espacios al principio y al final    "
print(s_texto11.strip())

# replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
print(s_texto12.replace("casa", "hogar"))

# join() reune todos los iterables de una lista con un string especifico
print(":".join(["Este" ,  "lugar" , "es" , "divertido"]))

# find() retorna la posición de la primera similitud de la substring
cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print(cadenaDeTexto.find('quien'))  # Devolvería: 52

# rfind() retorna la última posición de la similitud de la substring.
cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print(cadenaDeTexto.rfind('quien'))    # Devolvería: 94, Si, el substring no es encontrado retorna -1.

# replace. Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
miString = "Esto es bonito. Esto es bueno."
newString = miString.replace("es" ,"FUE")
print(newString)    # Devolvería: Esto FUE bonito. Esto FUE bueno.

#OPERADORES LOGICOS
#Operadores and, or, not
a = True
b = False
resultado1 = a and b
print(resultado1)   

resultado2 = a or b
print(resultado2)

resultado3 = not a
print(resultado3)

# Sintaxis simplificada para varios operadores lógicos
edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30     print(veintes)
veintes = edad >= 20 and edad < 30
if veintes: 
    print('veintes')

#treintas = edad >= 30 and edad <40     print(treintas)
treintas = edad >= 30 and edad < 40 
if treintas:
    print('treintas')

if ( 20<= edad <30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
else: 
    print('No esta dentro de los 20\'s ni los 30\'s')


if veintes:
    print('Dentro de los 20\'s')
if treintas:
    print('Dentro de los 30\'s')
else:
    print('Fuera de rango')

 
# % Módulo. Nos devuelve el resto de una división:

n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print("El resto de dividir" , n_numerador , "entre" , n_denominador , "es" , n_resto)

# ==  Igual que...; No confundir con el operador de asignación =
# Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.
n_numero7 = 34
s_texto7 = "34"
n_numero7 == s_texto7

n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3

# !=  Diferente que...
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5

# +=  Suma e incremento
n_numero6 = 34
n_numero6 += 1 #Sería como poner: n_numero6 = n_numero6 +1 
print(n_numero6)

#OBJETOS MUTABLES E INMUTABLES
# Obtener la dirección de memoria de una variable
a = 65
print("La dirección de memoria 1 es " , id(a))

# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria 2 es " , id(miNumero))
print("La dirección de memoria 3 es " , id(miNumero2))

# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a= 65
print("La dirección de memoria 4 es" , id(a))
a += 2
print("La dirección de memoria 5 es" , id(a))

# Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5, 6)
print("La dirección de memoria 6 es" , id(a))

# Obtener la dirección de memoria de una lista
a = (1, 2, 3, 4, 5, 6, 7)
print("La dirección de memoria 8 es" , id(a))
 
# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2, 'c': 3}
print(a)
print("La dirección de memoria 9 es" , id(a))

a["c"] = 3
print(a)
print("La dirección de memoria 10 es" , id(a))


#IF , ELIF, ELSE
# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.
notaIn = int(input("Introduzca nota: "))
if notaIn<5:
	calificacion = "Suspenso"
else: 
	calificacion = "Aprobado"
print(calificacion)

# IF no sólo evalúa un boleano, también si una variable contiene información
variable1 = 19
if variable1:
	print("Contiene información")
else: 
	print("No contiene informacion")
#En este ejemplo sí evalúa un boleano
if variable1 == True:
	print("Contiene Info")
else: 
	print("No contiene Info")
    
# Programa que pide una edad por consola y valora si el usuario es mayor de edad o no.
edad = int(input("Introduzca edad: "))
if edad<18:
	print("Es mmenor de edad")
elif edad>100:
	print("Edad incorrecta")
else: 
	print("Es mayor de edad")

# Programa que pide una nota por consola y valora las posibles calificaciones del alumno.
nota1 = int(input("Introduzca nota: "))
if nota1<5: 
	print("Suspenso")
elif nota1<7:
	print("Aprobado")
elif nota1<9: 
	print("Notable")
else: 
	print("Sobresaliente")

# IF abreviado
n_numero1 = 5
n_numero2 = 10
if n_numero1 > n_numero2: print(n_numero1 , "es mayor que " , n_numero2)

# IF...ELSE abreviado
a = 2
b = 330
print("A") if a> b else print("B")

# Se pueden concatenar operadores de comparación:
edad = 117
if 0<edad<100:  # Sería como poner: if edad>0 and edad<100	
	print("Edad correcta")
else:
	print("Edad incorrecta")

# Otro ejemplo de operadores de comparación concatenados
salarioPresidente = int(input("Introduzca salario de Presidente: "))
print("El salario del presidente es de " , salarioPresidente)

salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" , salarioDirector)

salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" , salarioJefe)

salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" , salarioOperario)

if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
	print("Todo correcto")
else: 
	print("Algo no va bien")

# Operadores AND y OR
distancia = int(input("Introduzca distancia: "))
numero_hermanos = int(input("Introduzca número de hermanos: "))
nota_media = int(input("Introduzca nota media: "))

if distancia<25 or numero_hermanos<2 or nota_media<5:
	print("No eres candidato a Beca")
else:
	print("Eres candidato a Beca")

if distancia>25 and numero_hermanos>2 and nota_media>5:
	print("Si eres candidato a Beca")

# Operador IN
opcion = input("Elige una opción: Opción1, Opción2, Opción3, Opción4: ")
pasoMinusculas = opcion.lower()
if pasoMinusculas in("Opción1" , "Opción2" , "Opción3" , "Opción4"):
    print("Opción válida: " + pasoMinusculas)
else:
	print("Opción Inválida: " + pasoMinusculas)
 
# If anidados. Queremos comprar un coche. Necesitamos ser mayores de edad y tener 20000€
n_edad = int(input("Introduce edad: "))
n_dinero_ahorrado = int(input("Introduce cantidad: "))
if n_edad <18: 
	print("No tienes edad suficiente")
else:
	if n_dinero_ahorrado <30000:
		print("Tienes la edad necesaria, pero no el dinero")
	else: 
		print("Puedes comprar el coche")

#OPERADOR TERNARIO
#Operador ternario
num = 12
var = "par" if (num % 2 == 0) else "impar"
print(var)

#Sería como escribir
nume = 12
if nume % 2 == 0:
	print("Par")
else: 
	print("Impar")










   

