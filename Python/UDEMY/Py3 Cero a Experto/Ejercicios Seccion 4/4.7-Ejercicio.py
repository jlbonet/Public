"""
### 7) Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:

+ ### Todos los números del 0 al 10 [0, 1, ..., 10]
+ ### Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
+ ### Todos los números pares entre el 0 al 20 [0, 2, 4, ..., 20]
+ ### Todos los números impares entre el -20 al 0 [-19, -17, -15, ..., -1]
+ ### Todos los números múltiplos de 5 del 0 al 50 [0, 5, 10, 15, ..., 50]
"""

print("Bienvenido al programa. Vamos a generar las siguientes listas: \n")

print("Lista1:")
lista1 = list(range(0, 11, 1))
print(lista1, "\n")

print("Lista2:")
lista2 = list(range(-10, 1, 1))
print(lista2, "\n")

print("Lista3:")
lista3 = list(range(0, 22, 2))
print(lista3, "\n")

print("Lista4:")
lista4 = list(range(-19, 1, 2))
print(lista4, "\n")

print("Lista5:")
lista5 = list(range(0, 55, 5))
print(lista5, "\n")