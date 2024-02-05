### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print(f"Mi condición es mayor o igual que {my_condition}")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

# For

my_list = [35, 24, 62, 52, 30, 30, 17]#Iteracion en lista

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brian", "Ramirez", "Brian")#iteracion en tupla

for element in my_tuple:
    print(element)

my_set = {"Brian", "Ramirez", 35}#iteracion en sets

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brian", "Apellido": "Ramirez", "Edad": 35, 1: "Python"}#iteracion en dicts

for element in my_dict:
    print(element)
    if element == "Edad" and my_dict[element]==35:
        print(f'Usted tiene {my_dict[element]} años')
        break
else:
    print("El bluce for para diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")