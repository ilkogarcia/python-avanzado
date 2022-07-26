def calcular_perimetro(*args):
    '''Calcular el perímetro de una figura geométrica
    
    Para ello se suman todos los lados de la figura que
    se suministran mediante argumentos de la función
    '''
    
    print(args)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro_triangulo = calcular_perimetro(2, 3, 5)
print(perimetro_triangulo)

perimetro_hexagono = calcular_perimetro(2, 3, 5, 3, 6, 3)
print(perimetro_hexagono)

