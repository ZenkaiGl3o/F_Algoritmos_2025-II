def ejer1():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:  #Dos puntos para cerrar un "if"
        print("Menor de edad")
    else:
        if edad >= 18 and edad <=64: #para &(and) se usa literalmente "and"
            print("Adulto")
        else:
            print("Adulto mayor")
def ejer2():
    ano = int(input("ingrese el año: "))

    if (ano %4 ==0 and ano %100 !=0) or (ano %400 ==0): #Parentesis no necesarios pero dan orden para la ejecucion :)
        print("\nEl año es bisiesto")
    else: 
        print("\nEl año no es bisiesto")    # \n al fin de la linea para bajar la respuesta

    if ano %2 ==0:
        print("el año es par")
    else:
        print("El año es impar")

def ejer3():
    Monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros\n")

    Opcion=int(input("Ingrese una opción: "))

    match Opcion:    # Es como switch de C#
        case 1: print("Dolares: ", round((Monto/3.75),2))
        case 2: print(f"Euros: {Monto/4.05:.2f}")
        case _: print("Opcion incorrecta :)")

import math

def ejer4():
    print("Bienvenido al sistema de calculos de áreas :)\n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            lado = int(input("Ingrese lado: "))
            print("Área: ", lado*lado)
        case 2:
            b4se = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Area rectangulo: ",(b4se*alt))
        case 3:
            b4se2 = int(input("Ingrese la base: "))
            alt2 = int(input("Ingrese la altura: "))
            print("Area rectangulo: ",(b4se2*alt2)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("Área del circulo: ",(round(math.pi * radio**2),2))  # Math.pow o x ** y para potencia
        case _: print("Opción incorrecta >:(")  

ejer4()