def Mostrar(_matriz, tipo_de_matriz) -> None:
    print(f"\n La matriz es la siguiente: {tipo_de_matriz}")
    for fila in _matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


def bandera_de_escocia(_matriz: list[str]) -> bool:
    posicion_de_ceros = (0, -1)
    casos_exitosos = 0
    cantidad_ceros = 0

    for index, columna in enumerate(_matriz):
        columna_limpia = columna.split(" ")
        cantidad_ceros = columna_limpia.count("0")

        if cantidad_ceros == 2 or cantidad_ceros == 1:
            if (columna_limpia[posicion_de_ceros[0]] == "0" and columna_limpia[posicion_de_ceros[1]] == "0" and index ==
                    posicion_de_ceros[0]):
                casos_exitosos += 1
                posicion_de_ceros = (posicion_de_ceros[0] + 1, posicion_de_ceros[1] - 1)
            else:
                break
        else:
            break

    if casos_exitosos == len(_matriz):
        return True

    return False


matriz = []

resultado = bandera_de_escocia(matriz)
cantidad_de_terminos = int(input(""))

for i in range(cantidad_de_terminos):
    matriz.append(input(""))
if resultado:
    print("Si es la bandera de Escocia")
else:
    print("No es la bandera de Escocia")
