def ejer1():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:  #Dos puntos para cerrar un "if"
        print("Menor de edad")
    else:
        if edad >= 18 and edad <=64: #para &(and) se usa literalmente "and"
            print("Adulto")
        else:
            print("Adulto mayor")

ejer1()