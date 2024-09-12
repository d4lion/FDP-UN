def Mostrar(_matriz):
    print("\n La matriz es la siguiente:")
    for fila in _matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


def obtener_producto(ls: list) -> int:
    producto = 1

    for l in ls:
        producto *= l
    return producto


def analizar_matriz(_matriz: list[list]) -> dict[str, dict[str, int]]:
    resultados = {
        "mayor_fila": {
            "indice": 0,
            "producto": obtener_producto(_matriz[0])
        },
        "menor_fila": {
            "indice": 0,
            "producto": obtener_producto(_matriz[0])
        }}

    for index, fila in enumerate(_matriz):

        producto_fila = obtener_producto(fila)

        if resultados['mayor_fila']["producto"] < producto_fila:
            resultados['mayor_fila']["indice"] = index
            resultados['mayor_fila']["producto"] = producto_fila

        if resultados['menor_fila']["producto"] > producto_fila:
            resultados['menor_fila']["indice"] = index
            resultados['menor_fila']["producto"] = producto_fila

    return resultados


filas = int(input())
columnas = int(input())
matriz = []

for i in range(filas):
    matriz_interna = []
    for j in range(columnas):
        elemento = int(input())
        matriz_interna.append(elemento)
    matriz.append(matriz_interna)

resultado = analizar_matriz(matriz)

print(resultado["mayor_fila"]["indice"])
print(resultado["menor_fila"]["indice"])



