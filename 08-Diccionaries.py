### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brian",
                 "Apellido": "Ramirez", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brian",
    "Apellido": "Ramirez",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_dict)
print(type(my_dict["Lenguajes"]))

print(my_other_dict)
print(len(my_other_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Brian" in my_dict)#Da falso porque esta busqueda es por llave
print("Apellido" in my_dict)#Por llave

# Inserción

my_dict["Calle"] = "Calle Central"
print(my_dict)#Si no existe se añade al final

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict)

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
#Hacer dicts con llaves basandose en listas o otras elementos
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))#La llaves son los elemntos de list
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_list, 'Para todos' )#Asignarle el mismo valor a todas las llaves
print((my_new_dict))

my_new_dict = dict.fromkeys((my_list))#La llaves son los elemntos de list
print(my_new_dict)

my_new_dict[my_list[0]]= 'Brian'
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))#Lista de los valores
print(tuple(my_new_dict))#Tupla de llaves
print(set(my_new_dict))#Set de llaves