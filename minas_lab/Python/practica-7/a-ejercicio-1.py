def cambiosDeLugar(lista_de_notas: list):
    cantidad_de_no_cambios = 0

    lista_de_notas_ordenada = sorted(lista_de_notas, reverse=True)

    for nota in range(0, len(lista_de_notas_ordenada)):
        if lista_de_notas_ordenada[nota] == lista_de_notas[nota]:
            cantidad_de_no_cambios += 1

    return cantidad_de_no_cambios


casos_de_prueba = int(input())

while casos_de_prueba > 0:

    cantidad_de_notas = int(input())
    notas = []

    for i in range(cantidad_de_notas):
        notas.append(float(input()))

    print(cambiosDeLugar(notas))

    casos_de_prueba -= 1
