"""
2
edad_persona -> edadPersona
ganancia_neta -> gananciaNeta
"""


def convertLowerToCamelCase(cadena: str):

    cadena_separada = cadena.split('_')
    lista_palabras_convertida = []

    for i in range(0, len(cadena_separada)):
        if i > 0:
            lista_palabras_convertida.append(cadena_separada[i].capitalize())
        else:
            lista_palabras_convertida.append(cadena_separada[i])

    cadena_camelcase = ''.join(lista_palabras_convertida)

    return cadena_camelcase


numer_de_casos = int(input())

while True:

    if numer_de_casos == 0:
        break

    numer_de_casos -= 1

    cadena = input()
    cadena_convertida = convertLowerToCamelCase(cadena)
    print(cadena_convertida)
