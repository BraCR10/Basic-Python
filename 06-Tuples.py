### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brian", "Ramirez", "Brian")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple#Devuelve una tupla con ambas
print(my_sum_tuple)

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)#Hacer la mismas tupla en lista o otra lista que sea igual a la tupla
print(type(my_tuple))

my_tuple_list = list(my_tuple)#O otra lista que sea igual a la tupla
print(type(my_tuple_list))

my_tuple_list = tuple(my_tuple)#Volver a ser una tupla 
print(type(my_tuple_list))
