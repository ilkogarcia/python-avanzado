import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "/Users/ilko/Documents/GitHub/python-avanzado/05_archivos_cvs/csv_vacio.csv"

ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)


# archivo_abierto = open(ruta, "w")
# witer = csv.writer(archivo_abierto, delimiter=",")
# archivo_abierto.close()
