"""
### 6) Realiza un programa que pida al usuario un número entero entre el 0 al 9, y que mientras el número no sea correcto se repite el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números [0,1,3,5,8] y notificarlo:
"""

import re


print("Bienvenido al programa.")

while True :
    
    selecion = input("Introduce un número del 0 al 9: ")
    
    if not re.match('^[0-9]$', selecion) :
        print("No has intrucido un número correcto. Por favor, repite el proceso.\n")
    else:
        break
    
lista_numeros = [0,1,3,5,8]

if selecion in lista_numeros :
    print( f"El número {selecion} existe en la lista de números")
        
else :
    print( f"El número {selecion} NO existe en la lista de números")
        
