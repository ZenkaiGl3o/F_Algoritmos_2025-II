from traceback import print_exception


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

def ejer3():
    n=int(input("Ingrese un numero: ")) 
    suma=0
    print()  #Linea vacia

    for i in range(1,n+1):  #Rango de numeros del 1 hasta n(valor variable o fijo)
        print(i)

        if i % 2 == 0:  #si i divido entre 2 da 0
            suma += i
    print("\nSuma de pares: ", suma)

def ejer4():

    cant=int(input("Ingrese la cantidad de numeros: "))
    ceros = pares = impares = 0
    print()
    for i in range(1, cant+1):
        num=int(input(f"Ingrese el numero{i}: "))

        if num==0:
            ceros+=1  #ceros++
        elif num %2==0:
            pares +=1 #pares++  
        else:
            impares +=1 # impar++
        
    print("\n#ceros: ",ceros)
    print("#pares: ",pares)
    print("#impares: ",impares)
                
def ejer5():      
    print()


ejer4()