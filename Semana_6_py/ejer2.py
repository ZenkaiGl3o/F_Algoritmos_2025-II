sumap = sumai = 0
while True:
    num=int(input("Ingrese un número positivo(0 salir): "))
    
    if num<0:
        print("Numero invalido. Ingrese nuevamente: ")
        continue #seguir ejecutando while asi sea falsa

    if num==0:
        break  #finalizar repetitiva
    if num%2 == 0:
        sumap += num
    else:
        sumai += num
    
print("\nSuma pares: ", sumap)
print("suma de impares: ", sumai)