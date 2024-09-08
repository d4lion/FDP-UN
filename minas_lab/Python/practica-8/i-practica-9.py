cantidad_casos = int(input())

while True:
    cantidad_machos = 0
    cantidad_hembras = 0

    if cantidad_casos == 0:
        break

    cantidad_casos -= 1

    cadena = input().split(' ')

    for cables in cadena:
        for cable in cables:
            if cable == 'M':
                cantidad_machos += 1
            else:
                cantidad_hembras += 1

    if cantidad_machos == cantidad_hembras:
        print('Circulo de cables')
    else:
        print('Circulo imposible')
