from turtle import st


class Video() :
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento) :
        
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        
        print("Se ha creado el video", self.titulo)
        
    # Redefinimos str para que muestre la información del video.
    def __str__(self) -> str:
        return f"{self.titulo} publicado en {self.lanzamiento} con una duración de {self.duracion} minutos"
        
    def __len__(self) :
        return self.duracion
        
    # Destructor de clase
    #def __del__(self) :
        #print("Se elimino el video", self.titulo)
        
pelicula1 = Video("Los Vengadores", 143, 2012)
pelicula2 = Video("Black Phanter", 134, 2018)

print(pelicula1.titulo)
print(str(pelicula2))
print(len(pelicula2))