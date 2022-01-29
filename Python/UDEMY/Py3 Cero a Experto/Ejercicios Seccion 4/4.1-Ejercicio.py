"""
# **4.4 Ejercicios**

</font>

### 1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
+  Mostrar la suma de dos números
+  Mostrar la resta de dos números (el primero menos el segundo)
+  Mostrar la multiplicación de dos números
### Si ingresamos una opción inválida, el programa informará que es incorrecto
"""

import re
from tkinter import N


print("\nBienvenido al programa.\n")

print("Debes introducir 2 números.\n")

contador_n1 = 0
contador_n2 = 0

   
while contador_n1 < 1 :

    numero1 = input("Por favor, introduce el primer número: ")
    
    if not re.match( '^([0-9]|[0-9].+)$', numero1 ) :
        print("No has introducido un número")
    else :
        print( f"El primer número introducido es: {numero1} \n" )
        contador_n1 += 1

while contador_n2 < 1 :

    numero2 = input("Por favor, introduce el segundo número: ")
    
    if not re.match( '^([0-9]|[0-9].+)$', numero2 ) :
        print("No has introducido un número")
    else :
        print( f"El segundo número introducido es: {numero2} \n" )
        contador_n2 += 1
contador = 0

numero1 = float(numero1)
numero2 = float(numero2)

while contador < 1 :

    print("************************************************************************************************")
    print("""Elige entre las siguientes opciones: \n
    1.- Mostrar la suma de los dos números introducidos.
    2.- Mostrar la resta del primer número introducido menos el segundo número introducido.
    3.- Mostrar la multiplicación de los dos números introducidos.
    4.- Salir
    """)
    print("************************************************************************************************\n")

    contador_o1 = 0

    while contador_o1 < 1 :
        
        opcion = input("Introduce la opción: \n")
        
        if not re.match( '^([0-9]|[0-9].+)$', opcion ) :
            print("No has intrducido una opción correcta")
        else :
            contador_o1 += 1
            continue
        
         
    if opcion == '1' :
        print( f"Se va a realizar la suma de los número introducidos, dando un resultado de: {(numero1) + (numero2)} \n")
    
    elif opcion == '2' :
        print( f"Se va a realizar la sustración del segundo número sobre el primero, dando un resultado de: {(numero1) - (numero2)} \n")
        
    elif opcion == '3' :
        print( f"Se va a realizar la multiplicación de los números, dando un resultado de: {(numero1) * (numero2)} \n" )
        
    elif opcion == '4' :
        print("Has elegido salir, hasta luego. \n")
        contador += 1