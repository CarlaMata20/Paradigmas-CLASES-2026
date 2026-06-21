from circulo import Circulo
from triangulo import Triangulo
import math

def test_area_del_circulo():
    radio = 2
    c = Circulo(radio)
    assert c.area() == math.pi * (radio **2) 

def test_area_del_triangulo():
    t = Triangulo(2, 5)
    assert (t.area() == 5.0)