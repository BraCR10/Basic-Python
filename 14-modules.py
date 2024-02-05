### Modules ###

#Importando pi del modulo math y poniendole el nombre de PI_VALUE
from math import pi as PI_VALUE
#llamando todo lo que haya en Math
import math
#Utilizando un modulo creado por mi que esta en la misma carpeta de este archivo y utilizando dos funciones que yo cree
from my_module import sumValue, printValue
#Importando todo el  modulo creado por mi
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))#potencia


print(round(PI_VALUE,3))