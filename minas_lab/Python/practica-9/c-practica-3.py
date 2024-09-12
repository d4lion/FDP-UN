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

    elementos_de_la_diagonal = []

    for index, fila in enumerate(_matriz):
        for index_f, columna in enumerate(fila):
            if columna != 0 and indentificador_matriz == index_f:
                """
                Columna: refiere al elemento de la matriz [fila][columna]
                indentificador_matriz: refiere a la columna y fila de la matriz donde está el elemento en la diagonal
                """
                elementos_de_la_diagonal.append(columna)
                casos += 1
                indentificador_matriz += 1

            elif columna != 0:
                cantidad_de_ceros_controller -= 1

    Mostrar(_matriz)

    """
    Si la cantidad de casos es igual a la longitud de la matriz y 
    la cantidad de ceros es igual a la cantidad de ceros
    """

    """
    Podemos saber si todos son iguales contando la longitud del arreglo de elementos de la diagonal
    y tomando cualquiera, si la longitud de esta lista es igual a la cantidad de elementos iguales
    cumple la condicion de ser escalar.
    """

    if elementos_de_la_diagonal.count(elementos_de_la_diagonal[0]) == len(elementos_de_la_diagonal):
        return "Matriz escalar"

    return "Matriz no escalar"


cantidad_de_terminos = int(input(""))
matriz = []

for i in range(cantidad_de_terminos):
    matriz_actual = []

    for j in range(cantidad_de_terminos):
        matriz_actual.append((int(input(""))))

    matriz.append(matriz_actual)

print(analizar_matriz(matriz))
