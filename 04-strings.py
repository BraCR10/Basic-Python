
# Formateo para imprimir mas rapido

name, surname, age = "Brian", "Ramirez", 18
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
#Se debe asignar todas las letras de la cadena
language = "python"
a, b, c, d, e,f= language
print(a)
print(e)

# División
language2 = "python2"
language_slice = language2[1:3]
print(language_slice)

language_slice = language2[1:]
print(language_slice)

language_slice = language2[-2]
print(language_slice)

language_slice = language2[0:7:2]#El tercer numero son los saltos
print(language_slice)

# Reverse
language3 = "python3"
reversed_language = language3[::-1]
print(reversed_language)


# Algunas Funciones del lenguaje para cadenas

print(language.capitalize())
print(language.upper())
print(language.count("t"))#Para contar la cantidad de veces que esta ese caracter en la cadena
print(language.isnumeric())#Es numerico?
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo