mayora0 = 0
menora0 = 0
igual = 0

for i in range(5):
    Num = int(input("Ingrese los numeros: "))
    if Num>0:
        mayora0=mayora0+1
    elif Num<0:
        menora0=menora0+1
    elif Num==0:
        igual=igual+1
    else:
        print("no")

print(f"Los numeros mayores a 0 son: {mayora0}")
print(f"Los numeros menores a 0 son: {menora0}")
print(f"Los numeros iguales a 0 son: {igual}")



