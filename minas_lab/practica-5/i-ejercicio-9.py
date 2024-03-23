cantidadNumeros: int = int(input())
listaNumeros: list = []


def ordenar_ascendente(lista: list) -> list:
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


for i in range(0, cantidadNumeros):
    listaNumeros.append(int(input()))

listaNumeros = ordenar_ascendente(listaNumeros)

if cantidadNumeros % 2 != 0:
    mediana: float = listaNumeros[(cantidadNumeros // 2)]
    print(mediana)
else:
    numeroMitad1: int = listaNumeros[cantidadNumeros // 2]
    numeroMitad2: int = listaNumeros[(cantidadNumeros // 2) - 1]

    mediana: float = (numeroMitad1 + numeroMitad2) / 2
    print(mediana)
