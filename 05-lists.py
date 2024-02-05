# Como definir una lista
my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Brian", "Ramirez"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda avanzadas
print(my_other_list[1])
print(my_other_list[-4])
print(my_list.count(30))#Contar la cantidad de veces que esta ese numero en la lista

print(my_other_list.index("Brian"))#Conseguir ubicacion de una cadena o numero, SUPER UTIL!

# Desempaqueado de elemnetos
#Se puede jugar con la equivalencias
age, height, name, surname = my_other_list
print(name)

name, height, age = my_other_list[2], my_other_list[1], my_other_list[0]
print(age)

#Uso interesante del .pop
print(my_list)
deleted_element = my_list.pop(2)#Podemos eliminar el elmento de la lista y asignar l elemnto eliminado a una variable z
print(deleted_element)
print(my_list)
#.pop() vacio elimina el ultimo

#Otras formas de eliminar
del my_list[2]#Por indice
print(my_list)
my_list.remove(30)#Por elemento que encuentra de izq a der
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()#Hace una copia en ese momento y se la asigna a la nueva lista

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()#Numeros o abecedario
print(my_new_list)

