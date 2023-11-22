
class Rectangulo:
        
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcular_Area(self):
        Area = self.alto * self.ancho
        return Area

    def calcular_Perimetro(self):
        p = (self.alto + self.ancho) * 2
        return p

rectangulo = Rectangulo(5,20)
print(rectangulo.alto)
print(rectangulo.ancho)
print(rectangulo.calcular_Area())
print(rectangulo.calcular_Perimetro())





