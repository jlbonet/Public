"""
### 4) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
+ Si los dos números son iguales
+ Si los dos números son diferentes
+ Si el primero es mayor que el segundo
+ Si el segundo es mayor o igual que el primero
"""
import re

contador1 = 0
contador2 = 0

while contador1 < 1 :
    numero1 = input( "Por favor introduce el primer número: " )
    if not re.match( '^([0-9]|[0-9].+)$', numero1 ) :
        print( "No has introducido un número.\n" )
    else :
        contador1 += 1

while contador2 < 1 :
    numero2 = input( "Por favor introduce el segundo número: " )
    if not re.match( '^([0-9]|[0-9].+)$', numero2) :
        print("No has introducido un número.\n" )
    else :
        contador2 += 1
        
print( "Se van a analizar los números.\n" )
print( "¿Los dos números son iguales?, " , bool(numero1 == numero2) , '\n' )
print( "¿Los dos números son diferentes?," , bool(numero1 != numero2) , '\n' )
print( "¿Es el primer número mayor que el segundo número?, " , bool(numero1 > numero2) , '\n') 
print( "¿Es el segundo número es mayor o igual que el primer número?, " , bool(numero2 >= numero1) , '\n')