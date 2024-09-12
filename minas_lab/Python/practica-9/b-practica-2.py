def Mostrar(_matriz):
    print("\n La matriz es la siguiente:")
    for fila in _matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


def analizar_matriz(_matriz):
    indentificador_matriz = 0
    casos = 0
    longitud_matriz = len(_matriz)
    cantidad_de_ceros = longitud_matriz ** 2 - longitud_matriz
    cantidad_de_ceros_controller = cantidad_de_ceros

    for index, fila in enumerate(_matriz):
        for index_f, columna in enumerate(fila):
            if columna != 0 and indentificador_matriz == index_f:
                """
                Columna: refiere al elemento de la matriz [fila][columna]
                indentificador_matriz: refiere a la columna y fila de la matriz donde está el elemento en la diagonal
                """

                casos += 1
                indentificador_matriz += 1

            elif columna != 0:
                cantidad_de_ceros_controller -= 1

    Mostrar(_matriz)

    """
    Si la cantidad de casos es igual a la longitud de la matriz y 
    la cantidad de ceros es igual a la cantidad de ceros
    """
    if longitud_matriz == casos and cantidad_de_ceros_controller == cantidad_de_ceros:
        return "Matriz diagonal"

    return "Matriz no diagonal"


cantidad_de_terminos = int(input(""))
matriz = []

for i in range(cantidad_de_terminos):
    matriz_actual = []

    for j in range(cantidad_de_terminos):
        matriz_actual.append((int(input(""))))

    matriz.append(matriz_actual)

print(analizar_matriz(matriz))
