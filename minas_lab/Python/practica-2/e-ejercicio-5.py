precioEscritorio = 1_200_000
cantidadComprada = int(input())

precioNeto = precioEscritorio * cantidadComprada
descuento = 0

if cantidadComprada < 5:
    descuento = precioNeto * 0.1

elif cantidadComprada >= 5 and cantidadComprada < 10:
    descuento = precioNeto * 0.2

else:
    descuento = precioNeto * 0.4

print(f"El valor a pagar por el cliente es ${precioNeto - descuento}")
