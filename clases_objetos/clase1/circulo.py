import math

class Circulo():
    # constructor de la clase circulo
    def __init__(self, un_radio):
        self.radio = un_radio 
    
    def area(self):
        return math.pi * self.radio**2
    
    def diametro(self):
        return self.radio * 2
    
    def color(self):
        return "rojo"
