"""
### 3) Realiza un programa que pida un número impar.
# Si el usuario no ingresa un número impar, debe repetirse el proceso hasta que ingrese un número válido
"""

contador = 0

while contador < 1 :
    numero_par = int(input("Introduce un número impar: "))
    
    if numero_par % 2 ==  0 :
        print("\nNo has introducido un número impar. Por favor, vuelve a introducir el número \n")
    else :
        print( f"Has intrducido el número {numero_par}, el cual es impar.")
        print("Programa finalizado \n")
        contador += 1