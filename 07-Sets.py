### Sets ###

# Definición

my_set = set()
my_other_set = {}
#Para que py sepa que es un set, se debe insertar los datos
my_other_set = {"Brian", "Ramirez", 35}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("BRACR")

print(my_other_set)  # Un set no es una estructura ordenada
my_other_set.add("BRACR")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Brian" in my_other_set)
print("Joss" in my_other_set)

# Eliminación

my_other_set.remove("Brian")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set


# Transformación, es set varia mucho, esto no es muy funcional

my_set = {"Brian", "Ramirez", 35}
my_list = list(my_set)
print(my_list)
print(my_list[1])



# Otras operaciones
my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))