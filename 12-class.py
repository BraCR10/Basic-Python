### Classes ###

# Definición
class MyEmptyPerson:#Clases siempre con Upper Camel Case
    pass  # Para poder dejar la clase vacía
print(MyEmptyPerson)

# Clase con constructor, funciones y popiedades privadas y públicas
class Person:
    def __init__(self, name, surname, alias="Sin alias"):#Constructor
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada debido a los __, para acceder a ella se usa un get

    def get_name(self):#Se usa self para hacer entender a Py que use datos del constructor
        return self.__name

    def walk(self):#Se usa self para hacer entender a Py que use datos del constructor
        print(f"{self.full_name} está caminando")


my_person = Person("Brian", "Ramirez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brian", "Ramirez", "BRACR")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "PACO (WEB)"
print(my_other_person.full_name)

my_other_person.full_name = 879
print(my_other_person.full_name)