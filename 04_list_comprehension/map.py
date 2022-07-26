'''
map() function returns a map object(which is an iterator)
of the results after applying the given function to each
item of a given iterable (list, tuple etc.)

Syntax:
map(fun, iter)

Parameters:
- fun: It is a function to which map passes each element
of given iterable.
- iter: It is a iterable which is to be mapped.

NOTE: You can pass one or more iterable to the map() function.

Returns:
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
 
NOTE: The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
'''

def calcular_cuadrado(numero):
    return numero**2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''lista_cuadrados = []

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)'''

map_cuadrados = list(map(calcular_cuadrado, lista_num))
print(map_cuadrados)
