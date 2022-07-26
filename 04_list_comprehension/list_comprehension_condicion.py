'''
lista = [ expresion(elemento) for elemento in objetoiterable if condición ]
lista = [ expresion(condición) for elemento in objeto_iterable ]
'''

def calcular_cuadrado(numero):
    return numero**2


def es_par(numero):
    return numero % 2 == 0

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print(lista_cuadrados)

# Crea una lista con el cuadrado de los números pares de una lista
lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print(lista_cuadrados_pares)

# Otra forma de crear una lista con el cuadrado de los números pares en una lista
lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print(lista_resultados)
