def Mostrar(_matriz, tipo_de_matriz) -> None:
    print(f"\n La matriz es la siguiente: {tipo_de_matriz}")
    for fila in _matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

def analizar_triangulo_superior(_matriz: list[list]) -> bool:
    """
    Esta función analiza si la matriz es triangular superior
    :param _matriz: Matriz a analizar si es triangular superior debe ser cuadrada ejemplo
    [[1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]]
    :return: True si es triangular superior, False si no lo es
    """
    cantidad_de_columnas_correctas = 0
    cantidad_ceros_por_columna = 0

    for index_columna, columna in enumerate(_matriz):
        ceros_columna_actual = columna.count(0)

        if cantidad_ceros_por_columna == ceros_columna_actual:
            cantidad_ceros_por_columna += 1
            cantidad_de_columnas_correctas += 1

    if cantidad_de_columnas_correctas == len(_matriz):
        return True

    return False


def analizar_triangular_inferior(_matriz: list[list]) -> bool:
    """
    Esta función analiza si la matriz es triangular inferior

    :param _matriz:  Matriz a analizar si es triangular
    inferior debe ser cuadrada ejemplo [[1, 0, 0], [2, 3, 0], [4, 5, 6]]
    :return: True si es triangular inferior, False si no lo es
    """
    cantidad_de_columnas_correctas = 0

    # Como es cuadrada el numero de columnas es igual al numero de filas
    cantidad_ceros_por_columna = len(_matriz) - 1  # <-- Esto es porque la diagonal no cuenta

    for index_columna, columna in enumerate(_matriz):
        ceros_columna_actual = columna.count(0)

        if cantidad_ceros_por_columna == ceros_columna_actual:
            cantidad_ceros_por_columna -= 1
            cantidad_de_columnas_correctas += 1

    if cantidad_de_columnas_correctas == len(_matriz):
        return True

    return False

def resultado_final(_matriz: list[list]) -> str:
    if analizar_triangulo_superior(_matriz):
        return "Triangular superior"
    elif analizar_triangular_inferior(_matriz):
        return "Triangular inferior"

    return "No es triangular superior ni inferior"


cantidad_de_terminos = int(input(""))
matriz: list[list] = []

for i in range(cantidad_de_terminos):
    matriz_actual = []

    for j in range(cantidad_de_terminos):
        matriz_actual.append((int(input(""))))

    matriz.append(matriz_actual)

print(resultado_final(matriz))



