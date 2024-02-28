"""
EL SALARIO DEL EMPLEADO

drive = https://drive.google.com/file/d/1uJyvcNbOJZ__A95hs0KxgNC3RPa3MBiR/view
"""


horasTrabajadas: int = int(input(""))
valorDeHoras: int = int(input(""))
totalPagar: int = 0

mensaje: str = "El empleado recibira un salario de $"

if horasTrabajadas <= 40:
    totalPagar = valorDeHoras * horasTrabajadas
    print(f"{mensaje}{totalPagar}")
else:

    horasExtra: int = horasTrabajadas - 40

    if horasExtra > 8:
        # Horas que sobrepasan las horas extra maxima que son 8
        horasExtraExcedentes = horasExtra - 8
        # Total a pagar para las hora extras excedidas que serán pagadas al triple
        totalPagar += (valorDeHoras * 3) * horasExtraExcedentes
        # Pago de las horas trabajadas normales
        totalPagarHorasNormales: int = valorDeHoras * 40
        # Pago de horas extra dentro del límite de las 8 horas
        totalPagarHorasExtra: int = (valorDeHoras * 2) * 8
        # Valor total de pago
        totalPagar += totalPagarHorasNormales + totalPagarHorasExtra
    else:
        totalPagar += (valorDeHoras * 40) + (valorDeHoras * 2) * horasExtra

    print(f"{mensaje}{totalPagar}")
