
"""
PAGO DEL PARQUEADERO

Un centro comercial cobra el parqueadero de la siguiente manera. Cada hora de parqueo se paga
con un 60% de descuento sobre el valor de una tarifa fija, siempre y cuando el vehículo haya
permanecido parqueado 5 horas o menos. La hora adicional de parqueo (a partir de la hora 6 en
adelante) se paga al 150% del valor de dicha tarifa.
Por ejemplo, si el valor de la tarifa fija es de $2000 y un vehículo tardó en el parqueadero del centro
comercial 8 horas, tendrá que pagar un total de $13000 ($4000 de las primeras 5 horas y $9000 de
las tres horas adicionales).
Escriba un programa para que dada una tarifa fija por hora de parqueo y la cantidad de horas que
pasa el vehículo en el parqueadero, se muestre el pago correspondiente.

ENTRADA
La entrada consta de dos líneas, cada una con un valor entero positivo. La primera línea para la tarifa
y la segunda línea para el número de horas.

SALIDA
Una sola línea con el valor a pagar (como valor entero) antecedido del símbolo $."""


costoDeParqueo: int = int(input(""))
horasDeParqueo: int = int(input(""))



if horasDeParqueo >= 5:
    
    # Calcula el descuento que se obtiene por las 5 horas que poseen un 60% de descuento
    descuento_de_parqueo = costoDeParqueo * 0.6

    # Se usa el descuento y se multiplica por las horas habiles que tienen en este caso 5
    costo_horas_sencillas = (costoDeParqueo - descuento_de_parqueo) * 5
    
    horas_excedentes = horasDeParqueo - 5

    # Se usa el costo de parqueo por el 150% por exceder 5 horas por el numero de horas que fueron excedidas
    costo_horas_excedentes = (costoDeParqueo * 1.5) * horas_excedentes
    totalAPagar = costo_horas_sencillas + costo_horas_excedentes

    print(f"${int(totalAPagar)}")
else:
    descuento_de_parqueo = costoDeParqueo * 0.6
    totalAPagar = (costoDeParqueo - descuento_de_parqueo) * horasDeParqueo

    print(f"${int(totalAPagar)}")