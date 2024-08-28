import os

path_actual = os.path.dirname(os.path.abspath(__file__))

with open(f'{path_actual}/utils/mensaje.txt') as file:
    ls = file.readlines()

    print(ls)

    lista_inversa = list(map(lambda x: x.replace('\n', '').strip()[::-1], ls))

    print(lista_inversa)

    print(lista_inversa)

    print('\n'.join(lista_inversa))
