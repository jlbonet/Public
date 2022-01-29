"""
### 5) Realiza una función llamada recortar() que reciba 3 parámetros. El primero es el número a recortar,
# el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente.
+ ### Devolver el límite inferior si el número es menor que éste
+ ### Devolver el límite superior si el número es mayor que éste
+ ### Devolver el número sin cambios si no se supera ningún límite.
"""

def recortar(a=None, lim_inf=None, lim_sup=None) :
    
    if a is None or lim_inf is None or lim_sup is None :
        return print("No ha introducido uno de los parámetros correctamente.")
    
    elif a < lim_inf :
        return lim_inf
    
    elif a > lim_sup :
        return lim_sup
    
    elif not a < lim_inf and not a > lim_sup :
        return a
    
print(recortar(23,7,25))
print(recortar(47,4,30))
print(recortar(32,70,250))
print(recortar(230,7,25))