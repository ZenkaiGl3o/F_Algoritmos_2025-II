import random

print("*************************************************")
print("*********Bienvenido al juego adivinador**********")
print("*                                               *")
print("*1. Adivinar el numero entre 1 y 20             *")
print("*2. Tienes 3 intentos                           *")
print("*************************************************")

intentos = 3
secreto = random.randint(1,20)  #Libreria para randomizar entre numeros

while intentos>0:
    num = int(input("\nIngrese numero: "))

    if secreto == num:
        print("\nCorrecto! Adivinaste el numero:)")
        break
    else:
        intentos -=1
        if num < secreto: print("\nPista: El numero es mayor. Intento", intentos)
        else: print("\nPista: El numero es menor. Intento", intentos)
else: print("No lograste nada. Fracasado. El numero es: ", secreto)