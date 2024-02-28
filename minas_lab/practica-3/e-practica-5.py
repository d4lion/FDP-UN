"""
EL TRIANGULO

drive: https://drive.google.com/file/d/14vZa_U2t8ybCmR9i4YmCHs_RPViBgNvI/view

RESUMEN:
A + B > C
A + C > B
B + C > A

"""


ladoA: float = float(input(""))
ladoB: float = float(input(""))
ladoC: float = float(input(""))


# Condiciones multiples en una sola linea de codigo
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:

    print("Los lados ingresados conforman un triangulo")

else:
    print("Los lados ingresados no conforman un triangulo")
