vocal=0
consonantes =1
for i in range(1,11):
    letra = input("Ingrese una letra: ")
    if letra=="a":
        vocal=vocal+1
    elif letra=="e":
        vocal=vocal+1
    elif letra=="i":
        vocal=vocal+1
    elif letra=="o":
        vocal=vocal+1
    elif letra=="u":
        vocal=vocal+1
    else:
        consonantes=consonantes+1

print(f"las letras vocales son: {vocal}")
print(f"las letras consonantes son: {consonantes}")


