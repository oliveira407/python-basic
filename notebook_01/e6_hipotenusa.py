import math


cateto1 = int(input("Ingrese el primer cateto "))
cateto2 = int(input("Ingrese el segundo cateto "))

hipotenusa = math.sqrt(cateto1 + cateto2) 

print("La hipotenusa es " + str(hipotenusa))
