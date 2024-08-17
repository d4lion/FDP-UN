ventas_diarias = [('MARTES', float(input())), ('MIERCOLES', float(input())), ('JUEVES', float(
    input())), ('VIERNES', float(input())), ('SABADO', float(input())), ('DOMINGO', float(input()))]

# La prueba finaliza el programa con un  -1
fin = input()

# Posicion 0: Dia de la semana y Posicion 1: Venta del dia
mayor_venta = ('', 0)

# se toma el valor de cualquier dato del array para evitar errores
menor_venta = (ventas_diarias[0][0], ventas_diarias[0][1])

# Total de ventas
total_ventas = 0

# Domingo supera total de ventas
domingo_supero_ventas = "SI"


for dia, venta in ventas_diarias:
    if venta > mayor_venta[1]:
        mayor_venta = (dia, venta)

    elif venta < menor_venta[1]:
        menor_venta = (dia, venta)

for dia, venta in ventas_diarias:
    if dia != 'DOMINGO':
        total_ventas += venta

if total_ventas / len(ventas_diarias) - 1 > ventas_diarias[-1][1]:
    domingo_supero_ventas = "NO"


print(mayor_venta[0], menor_venta[0], domingo_supero_ventas, end=" ")
