def cardsMoves(cartas: list):
    numero_de_cartas = len(cartas)
    orden_de_salida = []
    pos = 0

    while numero_de_cartas > 1:
        # Quita la carta que queda al inicio de la lista
        orden_de_salida.append(cartas.pop(0))

        # Mueve la carta que queda de primera a la ultima de la lista
        cartas.append(cartas[0])
        cartas.pop(0)

        numero_de_cartas -= 1

    return [cartas, orden_de_salida]

    


cantidad_de_cartas = 1

while cantidad_de_cartas > 0:
    cantidad_de_cartas = int(input())

    if cantidad_de_cartas > 2:
        lista_de_cartas = [i for i in range(1, cantidad_de_cartas + 1)]

        ultima_carta, orden_de_salida = cardsMoves(lista_de_cartas)

        print(*orden_de_salida, sep=', ')
        print(ultima_carta[0])