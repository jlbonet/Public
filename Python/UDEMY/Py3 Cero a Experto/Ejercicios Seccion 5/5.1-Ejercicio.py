"""
### 1) Realiza una función llamada area_rectangulo()
# que devuelva el área de un rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
"""

def area_rectangulo(a=None,h=None) :
    if a is None or h is None :
        print( "No ha introducido uno de los parámetros correctamente." )
    else :
        area_rectangulo_mensaje = print( f"El area del rectángulo es: {a*h} unidades\u00B2" )
        return area_rectangulo_mensaje
    
area_rectangulo( 15,10 )
    