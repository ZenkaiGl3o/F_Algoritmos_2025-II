from Triangulo import Triangulo
from Cuadrado import Cuadrado
t = Triangulo()
c = Cuadrado()

def menu1()->None:
    print("BIENVENIDO A CALCULOS DE AREAS Y PERIMETROS\n")
    print("1. Triangulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Trapecio")
    print("0. Salir")

def menu2()->int:
    print("SELECCIONE EL CALCULO A EJECUTAR")
    print("1. Área")
    print("2. Perímetro")

    opcion = int(input("Ingrese una opcion: "))
    return opcion

while True:
   menu1()
   while True:
       opcion = int(input("Ingrese opción: "))

       if opcion in (0,1,2,3,4): break
       else: print("Error. Opcion invalida.\n")

   match opcion:
       case 0: exit() #quit()
       case 1: 
           opc = menu2()

           match opc:
               case 1: t.area()
               case 2: t.perimetro()

       case 2:
           opc = menu2()
           l = int(input("Ingrese lado: "))
           match opc:
               case 1: c.area(l);
               case 2: c.perimetro(l);
       case 3: print()
       case 4: print()         
           
   while True:
       conti = input("¿Desea continuar? (s/n): ")
       if conti in("s", "n"): break
       else: print("Error. Solo ingrese 's' o 'n'.")

   if conti == "n": break 
