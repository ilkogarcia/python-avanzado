'''
lista = [ expresion(elemento) for elemento in objeto_iterable ]

list comprehension nos permiten crear listas de elementos en una
sola línea de código. Por ejemplo, podemos crear una lista con
los cuadrados de los primeros 5 números de la siguiente forma

cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]
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

# Ejemplo en el que vamos a determinar el número de "r" e una frase
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
print(len(erres))
#4