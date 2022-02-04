"""
### Crea una clase llamada _Punto_ con sus dos coordenadas X y Y.
+ Añade un método constructor para crear puntos, si no se recibe una coordenada, su valor será cero.
+ Redefine el método string para que al imprimir por pantalla el punto aparezca en formato (X,Y)
+ Define el método Cuadrante que indique a qué cuadrante pertenece el punto: 
<img src="https://robertoramirezblog.weebly.com/uploads/8/7/2/9/87295088/e70d9bdcdcab6e673b2c0356a02bdf6f_orig.jpg">
+ Define el método Vector, cuyos parámetros sean otro par de coordenadas y que calcule el vector que une los dos puntos.
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQGsL80EM7IlKq2eMT8Y98Niw8WvV14l54aag&usqp=CAU">
+ Define el método Distancia, cuyos parámetros sean otro par de coordenadas y que calcule la distancia entre los dos puntos y la muestre por pantalla. 
<img src="https://www.matesfacil.com/BAC/geometria2D/puntos/t6.png">

> PROTIP: En Python, la función raíz cuadrada se debe importar del módulo math y se llama sqrt().
"""

import math

class Punto :
    
    def __init__(self, x=0 , y=0) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def cuadrante(self) :
        if self.x > 0 and self.y >0 :
            cual_cuadrante = print(f"{self} pertenecen al Cuadrante I")
        elif  self.x < 0 and self.y >0 :
            cual_cuadrante = print(f"{self} pertenecen al Cuadrante II")
        elif  self.x < 0 and self.y <0 :
            cual_cuadrante = print(f"{self} pertenecen al Cuadrante III")
        elif  self.x >0 and self.y <0 :
            cual_cuadrante = print(f"{self} pertenecen al Cuadrante IV")
        elif self.x == 0 and not self.y == 0 :
            cual_cuadrante = print(f"{self} se ubica sobre el eje X")
        elif not self.x == 0 and self.y == 0 :
            cual_cuadrante = print(f"{self} se ubica sobre el eje Y")
        
        return cual_cuadrante
    
    def vector(self, numero) :
        print(f"El vector que une los puntos {self} y {numero} es igual a ({numero.x-self.x}, {numero.y-self.y})")

    def distancia(self, numero) :
        print(f"la distancia entre los puntos {self} y {numero} es igual a {math.sqrt(((numero.x-self.x)**2)+((numero.y-self.y)**2))}")
    

a = Punto(5,8)
b = Punto(10,2)
c = Punto(0,0)
d = Punto(4,0)

d.cuadrante()

a.vector(d)

a.distancia(b)

b.distancia(a)
  
    