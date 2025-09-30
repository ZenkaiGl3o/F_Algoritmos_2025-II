g = input("Genere una contraseña: ")

print("\nI------------------------------------------I")
print("I-----------Valida tu contraseña-----------I")
print("I------------------------------------------I")
print("I-------------Tiene 3 intentos-------------I")
print("I------------------------------------------I\n")

intentos = 3

while(intentos>0):
    c = input("Ingrese la contraseña: ")

    if g == c:
        print("\nAcceso concedido. Bienvenido al sistema.")
        break
    else:

        intentos-=1
        print("Contraseña incorrecta. Intentos restantes", intentos)

else: print("Acceso Denegado! Cerrando sistema") #Es else del while