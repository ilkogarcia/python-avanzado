'''
lista = [ expresion(elemento) for elemento in objeto_iterable ]
'''

def calcular_cuadrado(numero):
    return numero**2

def es_par(numero):
    return numero % 2 == 0

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []
for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)

print("Ciclo for", lista_cuadrados)

lista_comprehension = [calcular_cuadrado(num) for num in lista_num]
print("List comprehension", lista_comprehension)

lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print(lista_cuadrados_pares)


lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print(lista_resultados)

