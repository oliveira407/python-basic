import math


""""

#Ejercicio 1 


segundos = 86400
dias = int(input("Ingrese la cantidad de dias "))

resultado = dias * segundos

print("el resultado de la conversion en segundos es  " + str(resultado))



#Ejercicio 2


descuento = 10
monto = int(input("Ingrese su monto total"))

monto_desc = monto / descuento

resultado = monto - monto_desc

print("el descuento del monto total es  " + str(resultado))



#Ejercicio 3

Valor_del_euro = int(input("Ingrese su valor del euro "))
cantidad_en_dolares =  int(input("Ingrese su cantidad del dolar "))
cambio = cantidad_en_dolares * Valor_del_euro


print("el cambio total es " + str(cambio))




#Ejercicio 4 

edad_de_su_mascota = int(input("Ingrese edad de su mascota "))
edad_humana = 7
resultado = edad_de_su_mascota * edad_humana

print("la edad de su perro en edad humana es " + str(resultado)) 



#Ejercicio 5

peso = float(input("Ingrese su peso en kg "))
altura = float(input("Ingrese su altura en metros "))
imc = peso / (altura **2)   

print("su imc es " + str(imc))



#Ejercicio 7

curret_year = 2024
fecha_de_nacimiento = int(input("Ingrese su fecha de nacimiento "))
 
resultado = curret_year - fecha_de_nacimiento

print("su edad es " + str(resultado))



#Ejercicio 8





#EJERCICIO 9

cateto1 = int(input("Ingrese el primer cateto "))
cateto2 = int(input("Ingrese el segundo cateto "))

hipotenusa = math.sqrt(cateto1 + cateto2) 

print("La hipotenusa es " + str(hipotenusa))




nombre = str(input("Ingrese sus nombres "))
apellido = str(input("Ingrese sus apellidos "))

fijo = "@gmail.com"


print(str(nombre.lower())+str(apellido.lower()) + (str(fijo)))




enero = float(input("Ingrese su monto de gastos de enero "))
febrero = float(input("Ingrese sus monto de gastos de febrero "))
marzo = float(input("Ingrese su monto de gastos de marzo "))
abril = float(input("Ingrese su monto de gatos de abril "))

gastos = enero + febrero + marzo + abril

print("Tu gasto en estos 4 mese es " + str(gastos))

""""


edad = int(input("Ingrese su edad "))

if edad >= 0 and edad <= 12:
 print("Usted es un nene ")
 
if edad >= 13 and edad <= 17:
 print("Usted es un Adolecente ")

if edad >= 18 and edad <= 64:
 print("Usted es un Adulto ")

if edad >= 65 and edad <= 100:
 print("Usted es un Adulto Mayor ")


"""""


name = input("¿Cual es tu nombre?")
print(name)

age = ("¿cual es tu edad?") 
total = age + "10"

template = f"Hola mi nombre es {name}, tengo {age} edad y en 10 anos tendre {total} anos"

print(template)


"""

producto = int(input("Ingrese precio del producto "))
descuento1 = 



 