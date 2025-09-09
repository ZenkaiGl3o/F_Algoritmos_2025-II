def ejer1():
    nombre = input("Ingrese su name pe: ")  #Definir variable y leer los datos (se pueden los 2 a la vez)
    carrera = input("Ingrese su carrera: ")

    print(f"Hola {nombre}, bienvenido a FA de {carrera}") 
          #Imprimir es con print, y para concatenacion de interpolacion es una "f" antes de las comillas

def ejer2():
    print("\"Leonardo pe\"")  #Colocar comillas en un print (si quieres más comillas solo sigues aumentando barras )

def ejer3():
    x = int(input("Ingrese el valor de x pe: ")) #int sirve para definirlo como entero manualmente
    y = int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))    #Concatenar (usar texto y variables) en Python es con la coma
    print("Resta: ", (x-y))
    print("Multiplicación: ",(x*y))
    print("División: ", (x/y))

import math #importando libreria math (no incluida como en C#)

def ejer4():
    num = float(input("Ingrese un numero decimal pe: "))  #float es double en c#

    print("raiz 2: ", math.sqrt(num))
    print("redondeado: ", round(num,0)) #Al lado del num los decimales a los que se desea redondear
    print("al cubo: ",math.pow(num,3))
    print("raiz 3: ",num **(1/3)) #Conversion de raiz cubica para que sea leible en codigo / ** = es exponente

ejer4()