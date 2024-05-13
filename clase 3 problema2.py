print("Bienvenido a validacion de datos de la empresa XY")
user1 = input("ingrese el usuario: ")
userr = "pedro"
user2 = "angel"
if user1 == userr:
    print(f"bienvenido {userr}")
    contraseña = "1234"
    contraseña1 = input("INGRESE SU CONTRASEÑA: ")
    if contraseña1 == contraseña:
        print("contraseña correcta")
    else:
        print("contraseña incorrecta")
elif user1 == user2:
    print(f"Bienvenido {user2}")
    contraseña2 = "a4s1"
    contraseña22 = input("INGRESE SU CONTRASEÑA: ")
    if contraseña2 == contraseña22:
        print(f"Bienvenido {user2}")
    else:
        print("contraseña incorrecta")
else:
    print("ERROR USUARIO INCORRECTO")
    

    