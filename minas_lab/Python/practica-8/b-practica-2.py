def obtenerModeludo(lista_placas):

    valor = -9999
    modeludo = ''

    for placa in lista_placas:
        valor_temp = 0

        for digito in placa:
            valor_temp += ord(digito)

        if valor_temp > valor:
            valor = valor_temp
            modeludo = placa

    return modeludo


casos_de_prueba = int(input())

while True:

    if casos_de_prueba == 0:
        break

    casos_de_prueba -= 1

    placas = input().split()
    placaDeMiCarro = placas[0]

    carro_mas_modeludo = obtenerModeludo(placas)

    if placaDeMiCarro == "ONE999":
        print("Parece que hay otro vehiculo mas modeludo en el camino")
    elif carro_mas_modeludo == placaDeMiCarro:
        print("Estoy viajando en el vehiculo mas modeludo del camino")
    else:
        print(f"Parece que hay otro vehiculo mas modeludo en el camino")
