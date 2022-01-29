"""
### 4) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100
"""

contador = 0
lista_par = []
lista_impar = []

while contador < 101 :
            
    if contador % 2 ==  0 :
        lista_par.append(contador)
        contador += 1
        
    else :
        lista_impar.append(contador)
        contador += 1
        
resultado_par = sum(lista_par)

print(resultado_par)

# PROPUESTA

print(sum(list(range(0,101,2))))