'''
El operador de walrus es un operador de asignación con una funcionalidad extra.
El operador se representa con dos puntos seguidos de un igual :=, 
lo que tiene cierto parecido a una morsa, siendo : los ojos y = los colmillos,
por lo que de ahí viene su nombre (walrus significa morsa en Inglés).
'''


def calcular_cuadrado(numero):
    return numero ** 2


lista_num = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10]

lista_pares = []
for num in lista_num:
    # cuadrado = calcular_cuadrado(num)
    if (cuadrado := calcular_cuadrado(num)) % 2 == 0:
        lista_pares.append(cuadrado)
        # print(f"El cuadrado de {num} es {cuadrado}, y es un número par")
# else:
        # print(f"El cuadrado de {num} es {cuadrado}, y es un número impar")

print(lista_pares)

pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular_cuadrado(num)) % 2 == 0]
print(pares_comprehension)

