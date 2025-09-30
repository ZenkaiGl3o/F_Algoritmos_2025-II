while True:
   suma = 0
   num = int(input("Ingrese un numero positivo: "))

   for i in range(1,num+1):
       suma += i
       print(i, end=" ")

   print("\nSuma: ",suma)
   opc = input("¿Desea continuar?(S/N): ")
   
   if (opc =="N"): break