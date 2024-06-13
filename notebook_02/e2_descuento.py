confirmacion = True
total = 0 

while confirmacion == True:
    precio_producto = int(input("Ingrese el precio de su producto "))
    cantidad_producto = int(input("Ingrese la cantidad de su producto "))

    total += (cantidad_producto * precio_producto)
    descuento = 0 

    user = str(input("Desea comprar mas productos(SI/NO) "))
    user_upper = user.upper()
    if user_upper == "SI":
       confirmacion = True
    else: confirmacion = False   
    

if total >= 100 and total < 200:
    descuento = (10/100) * total
    total -= descuento
    print("Tu descuento es de 10% tu total a pagar es: " + str(total))
elif total >= 200:
    descuento = (20/100) * total
    total -= descuento
    print("Tu descuento es de 20% tu total a pagar es:" + str(total))
else: 
 print("Usted no tiene descuento")

        