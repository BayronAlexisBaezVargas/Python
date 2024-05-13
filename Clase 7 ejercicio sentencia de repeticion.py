#Definimos las variables / Ingresar datos

Num = int(input("Ingrese un numero para saber su tabla: "))
i=1
print(f"Tabla del {Num}")

#Sentencia de repeticion

for i in range(1,11):

    #Iniciamos el calculo calculo

    resu = Num*i

    #Mostrar los datos

    print(f"{Num} X {i} = {resu}")
#Ciclo While
print("\nCiclo while\n")
i=1
while (i<11):
    resu = Num*i
    print(f"{Num} X {i} = {resu}")
    i=i+1
