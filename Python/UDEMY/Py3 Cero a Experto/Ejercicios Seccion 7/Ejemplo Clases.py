class Torta :
    glaseado = False

    def __init__(self, sabor=None, color=None) :
        self.sabor = sabor
        self.color = color
        
        if sabor is None or color is None :
            print("Se ha creado un nuevo objeto torta")
        else :
            print(f"Se ha creado un nuevo objeto torta de {sabor} y {color}.")
        
        
    def glasear(self) :
        self.glaseado = True
        
    def esta_glaseada(self) :
        if (self.glaseado) :
            print("Soy una torta glaseada")
        else :
            print("Soy una torta NO GLASEADA")
        

torta = Torta("Fresa", "Roja")
torta2 = Torta()

print(torta.sabor)

print(torta.esta_glaseada())