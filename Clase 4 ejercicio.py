pregunta1 = int(input("Preguntas \n¿Como se llama el personaje principal de Dragon ball?\n(1). Vegeta\n(2). Yamcha\n(3). Bills\n(4). Ninguna es correcta\n----------\n"))
puntaje1 = 0
if pregunta1 == 1 or pregunta1 == 2 or pregunta1 == 3:
    print("")
elif pregunta1 == 4:
    puntaje1 = puntaje1 + 1
    print("")
else:
    print("Respuesta invalida se tomara mala")
pregunta2 = int(input("Pregunta 2\n¿Como se llama la esposa de vegeta?\n(1). Bulma\n(2). Milk\n(3). Maron\n(4). Bra\n-----------\n"))
if pregunta2 == 2 or pregunta2 == 3 or pregunta2 == 4:
    print("")
elif pregunta2 == 1:
    puntaje1 = puntaje1 + 1
    print("")
else:
    print("Respuesta invalida se tomara mala")
pregunta3 = int(input("Pregunta 3\n¿Cual es la tecnica mas utilizada por goku?\n(1). Makankosampo\n(2). Masenko\n(3). Galick Ho\n(4). KameKame Ha\n-----------\n"))
if pregunta3 == 1 or pregunta3 == 2 or pregunta3 == 3:
    print("")
elif pregunta3 == 4:
    puntaje1 = puntaje1 + 1
    print("")
else:
    print("Respuesta invalida se tomara mala")

if puntaje1 == 0:
    print("Su nota es 1.0")
elif puntaje1 == 1:
    print("Su nota es 2.7")
elif puntaje1 == 2:
    print("su nota es 4.5")
elif puntaje1 == 3:
    print("su nota es: 7.0")
print(f"puntaje: {puntaje1}")