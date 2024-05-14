#SETS Y CONJUNTOS

"""
Un conjunto es una colección de elementos únicos que no está ordenada ni indexada, 
por lo que no puede estar seguro de en qué orden aparecerán los elementos. 
En Python, los conjuntos se escriben entre llaves.
Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar nuevos elementos.
"""

# Declaración:
mi_set = {"Angel", "Sara", "Pilar"}
mi_set2 = {"Angel", "Manolo", "Juan"}

# Otra forma de declararlo
mi_set3 = set(("Angel", "Sara", "Juan"))
print(mi_set3)

# Para añadir un nuevo elemento:
mi_set3.add("Antonio")

# Para añadir varios elementos:
mi_set2.update({"Fran", "Pedro"})   

# Unión de colecciones. Si hay algún valor repetido sólo aparecerá una vez.
union = mi_set | mi_set2

# Intersección de conjuntos:
interseccion = mi_set2 & mi_set3

# Nos crea otro conjunto con los valores que estaban duplicados en ambos conjuntos.En nuestro caso sólo Angel.

# Diferencia de conjuntos. Nos crea otro conjunto con los elementos que no están duplicados.
diferencia = mi_set - mi_set2

# Para comprobar si un elemento está en un conjunto:
"Fran" in mi_set3	# Devuelve true o false

# Recorra el conjunto e imprima los valores:
mi_set4 = {"manzana", "banana", "cereza"}
for x in mi_set4:
  print(x)

"""
No puede acceder a los elementos de un conjunto haciendo referencia a un índice, 
ya que los conjuntos no están ordenados, los elementos no tienen índice.
"""

# Obtenga la cantidad de elementos en un conjunto:
mi_set4 ={"manzana", "banana", "cereza"}
print(len(mi_set4))

# Elimine "banana" utilizando el método remove() :
mi_set4 = {"manzana", "banana", "cereza"}
mi_set4.remove("banana")
print(mi_set4)

# Elimine "banana" utilizando el método discard() :
mi_set4 = {"manzana", "banana", "cereza"}
mi_set4.discard("banana")
print(mi_set4)

"""
Si el elemento a eliminar no existe, remove() generará un error.
Si el elemento a eliminar no existe, discard() NO generará un error.
"""

#   Elimine el último elemento utilizando el método pop() :
"""También puede usar el método pop() para eliminar un elemento, 
pero este método eliminará el último elemento. 
Recuerde que los conjuntos no están ordenados, 
por lo que no sabrá qué elemento se elimina.
"""
mi_set4 = {"manzana", "banana", "cereza"}
x = mi_set4.pop()
print(x)

print(mi_set4)

# El método clear() vacía el conjunto:
mi_set4 = {"manzana", "banana", "cereza"}

mi_set4.clear()

print(mi_set4)

# La palabra clave del borrará completamente el conjunto:
mi_set4 = {"manzana", "banana", "cereza"}

del mi_set4 
print(mi_set4)

# Unión de conjuntos
# El método union() devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:
mi_set5 = {"a", "b", "c"}
mi_set6 = {1, 2, 3}

mi_set7 = mi_set5.union(mi_set6)
print(mi_set7)

# El método update() inserta los elementos en set6 en set5:
mi_set5 = {"a", "b" , "c"}
mi_set6 = {1, 2, 3}

mi_set5.update(mi_set6)
print(mi_set5)

# Tanto union() como update() excluirán cualquier elemento duplicado.