'''
Sets comprehension
Son muy similares a las listas. La única diferencia es que debemos cambiar el () por {}.
'''

# En este ejemplo, creamos un SET con los números pares de la lista base
lista_num = [1, 2, 3, 4, 1, 2, 5, 6, 8]

set_pares = {num for num in lista_num if num % 2 == 0}
#{8, 2, 4, 6}
print(set_pares)

# En este ejemplo, si intentamos añadir un elemento que ya existe en el set,
# simplemente no se añadirá. Esto es porque los sets no admiten duplicados.
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
#{'r'}
print(mi_set)


'''
Dictionary comprehension
Son muy similares a los Sets Comprehension con la única diferencia que debemos especificar
la key o llave.
'''

# En este ejemplo, creamos un DICCIONARIO con las vocales de una cadena de texto
# En el diccionario, el nombre será la vocal en minuscula, y su valor la vocal en mayuscula
vocales = "aeiou"
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
# {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
print(diccionario)

# En este ejemplo estamos convirtiendo dos listas a un diccionario.
# Usado zip() podemis iterar dos listas paralelamente.
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
print(mi_dict)

