def ejer1():
    nombre = input("Ingrese su name pe: ")  #Definir variable, y leer los datos (funcionan así xd)
    carrera = input("Ingrese su carrera: ")

    print(f"Hola {nombre}, bienvenido a FA de {carrera}") 
          #Imprimir es con print, y para concatenacion de interpolacion es una "f" antes de las comillas

def ejer2():
    print("\"Leonardo\"")  #Colocar comillas en un print (si quieres más comillas solo sigues aumentando barras )

def ejer3():
    x = int(input("Ingrese el valor de x pe: ")) #int sirve para definirlo como entero manualmente
    y = int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))    #Concatenar (usar texto y variables) en Python es con la coma
    print("Resta: ", (x-y))
    print("Multiplicación: ",(x*y))
    print("División: ", (x/y))


ejer2()