def almacenar_datos(dato: str):
    global datos_productos

    dato = dato.split(":")

    datos_productos[dato[0]] = float(dato[1])


datos_productos: dict[str: int] = {}

cantidad_de_productos = int(input())

for i in range(cantidad_de_productos):
    producto = input()
    almacenar_datos(producto)

cantidad_de_compras = int(input())
valor_a_pagar = 0
descuento = 0

for j in range(cantidad_de_compras):
    producto_comprado = input()
    nombre_producto, cantidad_producto = producto_comprado.split(" ")

    valor_a_pagar += datos_productos[nombre_producto] * int(cantidad_producto)

if valor_a_pagar > 100_000:
    descuento = 0.3 * valor_a_pagar

print(valor_a_pagar - descuento)