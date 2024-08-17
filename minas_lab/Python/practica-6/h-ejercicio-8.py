from typing import Union


def cuadrante(cords_x: float, cords_y: float) -> Union[int, str]:

    # Si esta sobre el origen
    if cords_x == 0 and cords_y == 0:
        return 0
    # Detectar si se encuentra sobre alguna de las dos lineas
    elif cords_y == 0:
        return 'X'
    elif cords_x == 0:
        return 'Y'

    # Saber si es el cuadrante 1
    if cords_x > 0 and cords_y > 0:
        return 1
    # Saber si se encuentra en el cuadrante 2
    elif cords_x < 0 and cords_y > 0:
        return 2
    # Saber si se ecuentra en el cuadrante 3
    elif cords_x < 0 and cords_y < 0:
        return 3
    else:
        return 4


casos = int(input())

for i in range(casos):
    x = float(input())
    y = float(input())

    print(cuadrante(cords_x=x, cords_y=y))
