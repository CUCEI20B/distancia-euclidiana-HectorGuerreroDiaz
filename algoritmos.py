import math 

def distancia_euclidiana(x1,x2,y1,y2):
    res = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    return res
    """ Calcula la distancia euclidiana

    Devuelve el resultado de la formula

    También se le conoe a la fórmula como:
    distancia entre dos puntos

    Parámetros:
    x_1 -- origen_x
    y_1 -- origen_y
    x_2 -- destino_x
    y_2 -- destino_y

    """
    