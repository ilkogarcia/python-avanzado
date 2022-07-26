
'''
Las funciones lambdas se usan cuando se puede simplificar en una sola línea las instrucciones.
'''

def separar_par_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

    def calcular_area_cuadrado(lado):
        return lado ** 2
        
calcular_cuadrado= lambda lado:lado ** 2
print(calcular_cuadrado(2))

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
lista_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print (lista_pares)

nueva_lista = list(map(lambda numero: numero*10, lista_numeros))
print(nueva_lista)
