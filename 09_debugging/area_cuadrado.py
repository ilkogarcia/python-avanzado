def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado al recibir la longitud de sus lados"""
    area = lado*lado
    return area

lado_cuadrados = [1, 3, 5]
area_cuadrados = []
for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)
    area_cuadrados.append(area)

