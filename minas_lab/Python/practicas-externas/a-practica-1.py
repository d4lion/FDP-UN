def getUserNumbers():
    ls = []
    num = 1

    while True:
        num = int(input("Numero: "))
        if num != 0:
            ls.append(num)
        else:
            break

    return ls


def getSumImpares(ls: list[int]):

    suma = 0

    for index, elemento in enumerate(ls):
        if index % 2 != 0:
            suma += elemento

    return suma


def getPromedioPares(ls: list[int]):
    suma = 0
    elementos_sumados = 0

    for index, elemento in enumerate(ls):
        if index % 2 == 0:
            suma += elemento
            elementos_sumados += 1

    promedio = suma / elementos_sumados

    return round(promedio, 0)**2


def getMultiplyNumbers(n1: int, n2: int):
    return n1 * n2


lista = getUserNumbers()

sumaImpares = getSumImpares(lista)
promedioPares = getPromedioPares(lista)

print(getMultiplyNumbers(sumaImpares, promedioPares))
