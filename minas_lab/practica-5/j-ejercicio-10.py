tamanoListas: int = int(input())
elementosTotales: int = tamanoListas * 2
lista1: list = []
lista2: list = []
resultado: list = []
while elementosTotales > 0:
    numero: int = int(input())

    if tamanoListas < elementosTotales:
        lista1.append(numero)
    else:
        lista2.append(numero)

    elementosTotales -= 1

lista2 = lista2[::-1]

for index in range(0, len(lista1)):
    resultado.append(lista1[index] * lista2[index])

print(*resultado)