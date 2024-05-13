#declarar variables

lado = 5
#menu de opciones
while True:
   print("\n-----Menu de opciones-----\n")
   print("1.- Sumar dos numeros.")
   print("2.- Conocer un numero PAR.")
   print("3.- Dibujar un cuadrado.")
   print("4.- salir del programa.\n")

   try:
      opcion=int(input("Ingrese una opcion. "))
   except ValueError:
      print("equivocao")
   else:
    try:
       if opcion==1:
         print("Eligio la opcion 1 (Sumar dos numeros)")
         n1=int(input("Ingrese el primer numero: "))
         n2=int(input("Ingrese el segundo numero: "))
         resu=n1+n2
         print(f"el resultado de su suma es: {resu}")
       elif opcion==2:
         print("usted eligio la opcion 2 (Identificar un numero par)")
         num=int(input("Ingrese el numero que quiere identificar si es par: "))
         if num % 2 == 0:
            print("El numero es par")
         else:
            print("el numero es impar")
       elif opcion==3:
        print("usted eligio la opcion 3 (Dibujar un cuadrado)")
        for i in range(lado):
          for j in range(lado):
           if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
             print("*", end=" ")  
           else:
             print(" ", end=" ")
          print("")
       elif opcion==4:
        print("usted eligio la opcion 4")
        print("saliendo del programa")
        break
    except ValueError:
     print("equivocao")