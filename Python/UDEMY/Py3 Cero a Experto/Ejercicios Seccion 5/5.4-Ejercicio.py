"""
### 4) Realiza una funcion llamada intermedio() que a partir de dos puntos, devuelva su punto intermedio.
>  PROTIP: El número intermedio corresponde a la suma de los dos puntos entre dos.
"""

def intermedio(a=None, b=None) :
    
    if a is None or b is None :
        return print("No ha introducido uno de los parámetros correctamente.")
        
    else :
        return print( f"El punto intermedio de los números introducidos, {a} y {b}, es {(a+b)/2}")
    
intermedio(12, 14)
intermedio(500, 70)
intermedio(54, 314)
intermedio(712, 234)
intermedio(93, 63)

