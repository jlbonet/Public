class Videojuego :
    
    # COnstructor de clase.
    def __init__(self, titulo, genero, lanzamiento) -> None :
        self.titulo = titulo
        self.genero = genero
        self.lanzamiento = lanzamiento
        
        print("Se creó el videojuego: " , self.titulo)
        
    def __str__(self) -> str:
        return f"{self.titulo}, ({self.lanzamiento})"
    
class Catalogo :
    
    # Esta lista contendrá objetos de la clase videojuegos
    vjuegos = []
     
    def __init__(self, vjuegos=[]) -> None:
       self.vjuegos = vjuegos
        
    # V será un objeto de la clase videojuegos. 
    def agregar(self, v) :
       self.vjuegos.append(v)
        
    def mostrar(self) :
       for v in self.vjuegos :
           print(v) # Toma por defecto str(v) 
    
    
juego1 = Videojuego("The last of Us", "Acción", 2013)
print(str(juego1))

juego2 = Videojuego("The last of Us Part II" , "Acción" , 2020)

c = Catalogo([juego1, juego2])

c.mostrar()

c.agregar(Videojuego("Pokemon" , "RPG" , 1996))

c.mostrar()