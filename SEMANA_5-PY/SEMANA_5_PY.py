def ejer1():   #Anidada
    edad = int(input("Ingrese su edad puem: "))

    if edad >= 18:
        print("Puede votar miloco.")

        if edad >=25:
            print("Candidato para cargo politico.")
        else:
            print("No es candidato para ejercer un cargo politico")
    else:
        print("No puedes votar chibolo sano.")
        print("No puede ejercer un cargo politico.")
def ejer2():
    lado1 = int(input("Ingrese 1er lado: "))
    lado2 = int(input("Ingrese 2do lado: "))
    lado3 = int(input("Ingrese 3er lado: "))

    if (lado1 == lado2 == lado3):  #ESTO NO FUNCIONA EN C#
        print("EQUILATERO")
    elif lado1 == lado2 or lado1 == lado3 or lado2==lado3:
        print("ISOSCELES")
    else:
        print("ESCALENO")
        

ejer2()