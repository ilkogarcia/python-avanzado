'''
No siempre usar list comprehension es la mejor opción. En ocaciones es mejor usar las
instrucciones habituales de la programación
'''

'''Caso 1: No necesitamos el uso de una lista para conseguir el resultado'''
# Forma incorrecta
total = sum([num for num in range(10)])
print(total)

# Forma correcta
total = sum(num for num in range(10))
print(total)


'''Caso 2: No usar para imprimir una variable de un objeto iterable'''
# Forma incorrecta
[print(element) for element in range(10)]

# Forma correcta
for element in range(10):
    print(element)


'''Caso 3: Evitar el uso de ciclos anidados'''
# Forma incorrecta
lista_anidada = [[1,2], [3, 4], [5, 6]]
valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)

# Forma correcta
lista_anidada = [[1,2], [3, 4], [5, 6]]
valores_lista = []
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)
print(valores_lista)

