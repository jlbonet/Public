"""
### 3) Realiza una función llamada relacion() que a partir de dos numeros cumpla lo siguiente:
+ ### Si el primer número es mayor que el segundo, debe devolver 1
+ ### Si el primer número es menor que el segundo, debe devolver -1
+ ### Si ambos números son iguales, debe devolver 0
"""

def relacion(a=None,b=None) :

    if a is None or b is None :
        print("No ha introducido uno de los parámetros correctamente.")
        
    elif a > b :
        return 1
    
    elif a < b :
        return -1
    
    elif a == b :
        return 0
    
print(relacion(1,1))
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))