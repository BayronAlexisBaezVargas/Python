
try:
    num1=int(input("INGRESE UN NUMERO: "))
    num2=int(input("INGRESE OTRO NUMERO: "))
    resultado = round(num1/num2,2)
except ZeroDivisionError:
    print("Cantekbron no se puede dividir por 0")
except TypeError:
    print("COMO QUE UNA LETRA SEÑOR QUE ESTA HACIENDO")
except ValueError:
    print("debe ingresar un numero valido")
else:
    print(f"Resultado es: {resultado}")    
