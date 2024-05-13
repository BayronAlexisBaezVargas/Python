#PEDIMOS al usuario que ingrese sus datos
nombre=input("ingrese su nombre: ");
rut=(input("ingrese su Rut (Ej.11.111.111-1): "));
correo=input("ingrese su correo (Ej: aaa@Gmail.com):");
telefono=input("ingrese su telefono: ");

#Mostrar los datos
print(f"Nombre: {nombre.upper()} \nRUT: {rut} \nCORREO: {correo.upper()} \nTELEFONO: {telefono}");
