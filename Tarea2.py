#declarar la variables
totalPagar=0
cantidad=0
descuento=0.1 #Descuento del 10%

#Mostrar informacion
print("Bienvenido a la sandwicheria onde el Indio")
print("Lista de precios:")
print("1.- Churrascos----$1500\n2.- Completos----$1000\n3.- Vegetariano----$2000\n4.- Barros Lucos----$3000")
opcion=int(input("elija su comida: "))

#De acuerdo a la seleccion del usuario, hacer las condiciones
if (opcion==1):
    print("Eligio la opcion churrasco")
    cantidad = int(input("¿Cuantos churrascos quiere?: "))
    totalPagar=cantidad*1500
elif (opcion==2):
    print("Eligio la opcion Completos")
    cantidad = int(input("¿Cuantos completos quiere?: "))
    totalPagar=cantidad*1000
elif (opcion==3):
    print("Eligio la opcion vegetarianos")
    cantidad = int(input("¿Cuantos vegetarianos quiere?: "))
    totalPagar=cantidad*2000
elif (opcion==4):
    print("Eligio la opcion Barros lucos")
    cantidad = int(input("¿Cuantos Barros Lucos quiere?: "))
    totalPagar=cantidad*3000
else:
    print("Mal error fuera hechao del local nunca mas vuelva")

#Mostrar el total y preguntar si hay descuento
print(f"Usted debe pagar es de ${totalPagar}")
respuesta = input("Usted tiene un codigo de descuento del 10%? (si/no)\n")

#verificar la condicion del descuento
if (respuesta == "si"):
    totalPagar=totalPagar-(totalPagar*descuento)
    print("usted Tiene un descuento del 10% para el total de su compra")
elif (respuesta == "no"):
    print("Usted no tiene descuento.")
else:
    print("equivocao")

#mostrar denuevo el total
print(f"Total a pagar es de ${totalPagar}")
print("Ojala No vuelva buen dia :D..........")