import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]


datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

# Esta es una de las formas de crear un archivo nuevo y escribir en el
# archivo = open("datos.csv", "w")
# writer = csv.writer(archivo, delimiter=",")
# archivo.close()

# Esta es otra forma más elegante de crear un archivo.
# Ejemplo para escribir una sola línea de datos con writerow()
#with open("dato.csv", "w") as archivo:
#    writer = csv.writer(archivo, delimiter=",")
#    writer.writerow(columnas)
#    writer.writerow(dato)

# Ejemplo para escribir varias líneas de datos con writerows()
#with open("dato.csv", "w", newline = "") as archivo:
#    writer = csv.writer(archivo, delimiter=",")
#    writer.writerow(columnas)
#    writer.writerows(datos_lista)

# Ejemplo para escribir varias líneas de datos desde una lista de diccionario
with open("datos.csv", "w", newline = "") as archivo:
    writer = csv.DictWriter(archivo, fieldnames = columnas)
    writer.writeheader()
    writer.writerows(datos_dict)

