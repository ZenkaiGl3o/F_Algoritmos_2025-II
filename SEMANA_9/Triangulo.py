class Triangulo:
    def area(self)->None: #Self es para crear un metodo, y none para establecerlo como vacio(Void en C#)
        b=int(input("\nIngrese la base: "))
        h=int(input("\nIngrese la altura: "))
        print("\tArea: ", (b*h)/2)
    def perimetro(self)->None:
        l1=int(input("\nIngrese lado 1: "))
        l2=int(input("Ingrese lado 2: "))
        l3=int(input("Ingrese lado 3: "))
        print("Perimetro: ", l1+l2+l3)