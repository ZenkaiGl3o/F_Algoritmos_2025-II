num=int(input("Ingrese un numero positivo: "))
print()

while num<=0:  #While es repetitiva
    num=int(input("Error. Ingrese un numero positivo: "))
i  = 1
while i <=12:
    print(f"{i} x {num} = {i*num}")
    i+=1
