"""
### 5) Realiza un programa que pregunte al usuario cuántos números quiere introducir.
# Luego debe leer todos los números y obtener la media aritmética:
"""

print("Bienvenido al programa.")

numero_seleccion = int(input("¿Cuantos números desea introducir para realizar la media aritmética?: \n"))

contador = 1

lista_aritmetica = []

while contador <= numero_seleccion :
    lista_aritmetica.append(float(input( f"Introduce el numero {contador} ")))
    contador += 1
    
print( f"Ha introducido los siguientes números {lista_aritmetica} ")
print( f"Se va a realizar la media artimética de los número introducidos, dando un resultado de: {(sum(lista_aritmetica)/numero_seleccion)}")