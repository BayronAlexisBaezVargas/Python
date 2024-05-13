#Definir las variables
desFON = 0
fonasa = 0
sueldoliquido = 0
Totaldescu = 0
Sueldo = 0
#Desarrollo
while True:
    try:
        Nombre = input("Ingrese su nombre de usuario: ")
        Sueldo = int(input("Ingrese su sueldo en bruto: "))
    except TypeError:
        print("SE EQUIVOCOOOO")
    except ValueError:
        print("equivocado señor")
    except ZeroDivisionError:
        print("COMO LOGRO DIVIDIR POR CERO?")
    else:
        desAFP = Sueldo*0.10
        desFON = Sueldo*0.20
        afp = Sueldo-desAFP
        fonasa = Sueldo-desFON
        sueldoliquido = Sueldo+desAFP+desFON
        Totaldescu = desAFP + desFON
        print("--------------------------------")
        print("---Liquidacion de Sueldo---")
        print("--------------------------------")
        print(f"Sueldo en Bruto: {Sueldo}\nDescuento AFP (10%): {desAFP}\nDescuento FONASA (20%): {desFON}\nTotal descuentos: {Totaldescu}\nSueldo Liquido: {sueldoliquido}")
        print("--------------------------------")
        print("Desea liquidar otro sueldo? \n(1). Si\n(2). No")
        Resp = int(input("Ingrese su respuesta: "))
        if Resp==1:
            print("OK")
        elif Resp==2:
            print("tenga lindo dia")
            break
        else:
            print("opcion no valida")
with open ("Archivo.txt", "w") as archivo:
    archivo.write(f"Sueldo en Bruto: {Sueldo}\nDescuento AFP (10%): {desAFP}\nDescuento FONASA (20%): {desFON}\nTotal descuentos: {Totaldescu}\nSueldo Liquido: {sueldoliquido}")