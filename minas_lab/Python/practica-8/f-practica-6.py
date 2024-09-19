from os import path

path_actual = path.dirname(path.abspath(__file__))


with open(f'{path_actual}/utils/palabras.txt') as file:
    ls = file.readlines()
    file.close()

print(ls, file=open(f'{path_actual}/utils/ls.txt', 'w'))

# Se separan las palabras por espacios y se eliminan los saltos de linea y espacios en blanco
ls_clean = list(map(lambda x: x.replace('\n', '').strip().split(' '), ls))


for traduccion_de_palabras in ls_clean:
    ultima_terminacion = ''
    cumplen = 0

    for index, palabra in enumerate(traduccion_de_palabras):
        try:
            # Caso 1: Tomando las 2 ultimas letras de la palabra
            if palabra[-2:] == traduccion_de_palabras[index + 1][:2]:
                cumplen += 1
            # Caso 2: Tomando las 3 ultimas letras de la palabra
            elif palabra[-3:] == traduccion_de_palabras[index + 1][:3]:
                cumplen += 1
        except IndexError:
            pass

    if cumplen == len(traduccion_de_palabras) - 1:
        print('Cadena completa')
    else:
        print('Cadena rota')
