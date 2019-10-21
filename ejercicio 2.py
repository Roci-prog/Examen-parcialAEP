#Hacer que el sisteme genere un numero aleatorio entre 1 y 10. 
# luego hacer que el ususario adivine el numero. La aplicacion debe terminar cuando el ususario adivine.

import random,os
os.system("cls")

s = random.randint(1, 10)

while True:
    n = int(input("adivina el numero del sitema(1,,10):"))
    if n == s:
        print("Adivinaste!")
        break
    else:
        print("numero incorrecto")