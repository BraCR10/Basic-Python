### Functions ###

# Definición
def my_function():
    print("Esto es una función")
my_function()

# Función con parámetros de entrada/argumentos
def sum_two_values(first_value: int, second_value):#Asignarle el tipo de dato es poco util en Py
    print(first_value + second_value)
sum_two_values(5, 7)
sum_two_values("5", "7")

# Función con parámetros de entrada/argumentos y retorno
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum
my_result = sum_two_values_with_return(1.4 ,5.6)
print(my_result)

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")
print_name(surname="Ramirez", name="Brian")#Si usas clave tienes que asignar todos!

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Brian", "Ramirez")

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*parametrosIndefinidos):#El * permite pasar cualquier cantidad de parametros dentro de una funcion
    print(type(parametrosIndefinidos))
    for text in parametrosIndefinidos:
        print(text.upper())


print_upper_texts("Hola", "Python", "BRACR")
print_upper_texts("Hola")