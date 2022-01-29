"""
### 2) Realiza una función llamada área_círculo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 ancho
PROTIP: Utiliza el módulo math con la línea _import math_
"""
import math

def area_circulo(a=None) :
    if a is None :
        print( "No ha introducido uno de los parámetros correctamente." )
    else :
        calculo_Area_circulo = ((math.pi/4)*(a**2))
        area_circulo_mensaje = print( f"El area del círculo es: {calculo_Area_circulo} unidades\u00B2" )
        return area_circulo_mensaje
    
area_circulo(5)