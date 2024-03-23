"""
EL CAJERO

drive = https://drive.google.com/file/d/1xzRiDF_BoBuzZzQLgzLH-u2KVIPRvbxm/view

resumen(
devolver la cantidad minima de billetes
al hacer un retiro en un cajero
"""

valorRetiro: int = int(input())

valorSumaRetirado: int = 0

billetes: [int, int] = {}


while True:
    if valorRetiro > 50_000:
        cantidadBilletes = valorRetiro // 50_000
        billetes[50_000] = cantidadBilletes
        valorSumaRetirado += cantidadBilletes * 50_000
        valorRetiro -= valorSumaRetirado

    elif 20_000 <= valorRetiro < 50_000:
        cantidadBilletes = valorRetiro // 20_000
        billetes[20_000] = cantidadBilletes
        valorSumaRetirado = cantidadBilletes * 20_000
        valorRetiro -= valorSumaRetirado

    elif 20_000 > valorRetiro >= 10_000:
        cantidadBilletes = valorRetiro // 10_000
        billetes[10_000] = cantidadBilletes
        valorSumaRetirado = cantidadBilletes * 10_000
        valorRetiro -= valorSumaRetirado

    elif 10_000 > valorRetiro >= 5_000:
        cantidadBilletes = valorRetiro // 5_000
        billetes[5_000] = cantidadBilletes
        valorSumaRetirado = cantidadBilletes * 5_000
        valorRetiro -= valorSumaRetirado

    elif 5_000 > valorRetiro >= 2_000:
        cantidadBilletes = valorRetiro // 2_000
        billetes[2_000] = cantidadBilletes
        valorSumaRetirado = cantidadBilletes * 2_000
        valorRetiro -= valorSumaRetirado

    elif 2_000 > valorRetiro >= 1_000:
        cantidadBilletes = valorRetiro // 1_000
        billetes[1_000] = cantidadBilletes
        valorSumaRetirado = cantidadBilletes * 1_000
        valorRetiro -= valorSumaRetirado
    else:
        break

for valorBillete, cantidad in billetes.items():
    print(f"{cantidad} de ${valorBillete}")
