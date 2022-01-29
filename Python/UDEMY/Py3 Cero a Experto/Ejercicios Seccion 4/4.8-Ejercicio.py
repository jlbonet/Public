"""
### 8) Dadas dos listas, se debe generar una tercera lista con todos los elementos
# que se repitan en ellas, pero no debe repetir ningún elemento en la nueva lista.
lista_1 = ["M","i","","a","m","i","g","o","","G","a","l","i","l","e","o"]

lista_2 = ["T","u","","a","m","i","g","u","i","t","o"]

lista_3 = []
"""

lista_1 = ["M","i","","a","m","i","g","o","","G","a","l","i","l","e","o"]
lista_2 = ["T","u","","a","m","i","g","u","i","t","o"]
lista_3 = []
conjunto = set()

for l in lista_2 :
    if l in lista_1 :
        conjunto.add(l)

lista_3.append(conjunto)

print(lista_3)