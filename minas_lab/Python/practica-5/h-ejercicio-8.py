identificacionesPares: list = []
identificacionesImpares: list = []


def ordenar_ascendente(lista: list) -> list:
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_descendente(lista: list) -> list:
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


while True:
    identificacion: int = int(input())

    if identificacion < 0:
        break

    if identificacion % 2 == 0:
        identificacionesPares.append(identificacion)
    else:
        identificacionesImpares.append(identificacion)


print(*ordenar_ascendente(identificacionesPares), *ordenar_descendente(identificacionesImpares))
