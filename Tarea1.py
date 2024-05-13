print("Elija una opcion: ")
print("(1). dolar australiano a chileno")
print("(2). peso argentino a peso chileno")
print("(3). Yen a peso chileno")
print("(4). Salir")
menu = int(input("Ingrese su respuesta: "))
if menu == 1:
    print("Dolar australiano a chileno")
    ChilenaM = int(input("Ingrese cantidad de dolar australiano: "))
    Total = ChilenaM*619.08
    print(f"El resultado es: {Total}")
elif menu == 2:
    print("Peso argentino a peso chileno")
    ARG = int(input("Ingrese cantidad de peso argentino: "))
    Total1 = ARG*1.09
    print(f"El resultado del cambio es: {Total1}")
elif menu == 3:
    print("Yen a pesos chileno")
    Yen = int(input("Ingrese cuantos Yen: "))
    total2 = Yen*6.16
    print(f"El resultado del cambio es: {total2}")
elif menu == 4:
    print("saliendo del programa")
else:
    print("Opcion no valida")

