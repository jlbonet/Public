"""
1) Define una variable edad y asígnale un valor entero. 
+ Muestra su valor por pantalla.
+ Define otra variable edad_cadena que contenga el valor de edad como una cadena de caracteres. 
+ Comprueba el tipo de la nueva variable.
+ Utiliza la variable edad que has definido previamente y calcula la edad que tendría esa persona en el año 2035.
"""

import time

edad = 38
edad_str = str(edad)
año_actual = int(time.strftime('%Y'))
año_futuro = 2035
calculo__edad = (año_futuro - año_actual) + edad

print(edad)
print(type(edad_str))
print(calculo__edad)