while True:

    unidadesCompradas: int = int(input())

    if unidadesCompradas < 0:
        break

    precioProducto: float = float(input())

    # Calcular precio 3x2
    precioOferta3x2: float = round(precioProducto * (((unidadesCompradas // 3) * 2) + (unidadesCompradas % 3)))

    # Calcular precio 30%
    precioOferta30: float = round((precioProducto * unidadesCompradas) - (unidadesCompradas * precioProducto * 0.3))

    if precioOferta3x2 <= precioOferta30:
        print(f"Mejor oferta 3x2: ${precioOferta3x2}")
    else:
        print(f"Mejor oferta 30%: ${precioOferta30}")




