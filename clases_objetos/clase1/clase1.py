
import math

# Representar un circulo

radio = 2
# para calcular su area.

def area_del_circulo(radio):
    return math.pi * radio**2

print("area del circulo:")
print(area_del_circulo(radio))





# Representar un cuadrado 

lado = 4

def area_del_cuadrado(lado):
    return lado**2

print("area del cuadrado")
print(area_del_cuadrado(lado))

# Representar un rectangulo
base = 2
altura = 4

def area_del_rectangulo(base, altura):
    return base * altura

print("area del rectangulo")
print(area_del_rectangulo(base, altura))



# si es forma=circulo o forma=cuadrado, leo argumentos[0] para obtener radio/lado
# si es forma=rectangulo, leo argumentos[0] para la base y argumentos[1] para la altura
def area(forma, argumentos):
    if forma == "circulo":
        radio = argumentos[0]
        return area_del_circulo(radio)
    if forma == "cuadrado":
        lado = argumentos[0]
        return area_del_cuadrado(lado)
    if forma == "rectangulo":
        base = argumentos[0]
        altura = argumentos[1]
        return area_del_rectangulo(base, altura)
    if forma == "triangulo":
        base = argumentos[0]
        altura = argumentos[1]
        return (area_del_rectangulo(base, altura)/2)

print(area("circulo", [20]))
print(area("cuadrado", [5]))
print(area("rectangulo", [10, 50])) 

# Problemas de la solucion:
# 1. es dificil de usar correctamente.
# 2. no es facil de extender.

# hola