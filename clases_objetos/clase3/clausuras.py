
A = 3 

def devolver_mayor(x,y):
    z = 10000
    f = lambda x: x * A + z

    if x > y:
        return f(x)
    else: 
        return y


# print(devolver_mayor(2, 1))


# Map: permite abstraer ciclos del tipo
# for x in lista
#   f(x)

# filter
lista_filtrada = [] 
lista = [11, 22, 56, 89]
for x in lista:
    if x % 2 == 0: # criterio
        lista_filtrada.append(x)

print(lista_filtrada)
print(list(filter(lambda e: e % 2 == 0,lista)))



# filter
# permite abstraer ciclos for de este tipo
# resultado = []
# for x in lista:
#     if criterio(x):
#         resultado.append(x)

# all
print(all( map(lambda x: x % 2 == 0, [2,4]) ))
# any
print(any( map(lambda x: x % 2 != 0, [2,4,1]) ))

