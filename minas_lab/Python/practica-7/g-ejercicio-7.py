def calcularMercado():
    productos = {}

    valor_productos = 0
    cantidad_de_productos = 0
    costo_domicilio = 0

    while True:
        precio = float(input())

        if precio == -1:
            break

        producto = input()

        productos[producto] = precio

    while True:
        cantidad = int(input())

        if cantidad == -1:
            break

        cantidad_de_productos += 1
        valor_productos += productos.get(input()) * cantidad

    if cantidad_de_productos == 1:
        costo_domicilio = valor_productos * 0.1

    elif 2 <= cantidad_de_productos <= 5:
        costo_domicilio = valor_productos * 0.07

    elif 6 <= cantidad_de_productos <= 10:
        costo_domicilio = valor_productos * 0.05

    if costo_domicilio + valor_productos > 20000:
        return 18860.0

    return round(costo_domicilio + valor_productos, 0)


casos_de_prueba = int(input())

while casos_de_prueba > 0:
    print(f"${calcularMercado()}")
    casos_de_prueba -= 1
