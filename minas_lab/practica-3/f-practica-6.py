"""
EL TRIANGULO MEJORADO

drive = https://drive.google.com/file/d/1BJY63_Yx7SzTpE5X-ioN8sDd5KIuXf-9/view

RESUMEN:
determinar si el triangulo es escaleno, isoceles, equilatero
"""

ladoA: float = float(input(""))
ladoB: float = float(input(""))
ladoC: float = float(input(""))

msg = "Los lados ingresados conforman un triangulo"

# Condiciones multiples en una sola linea de codigo
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:

    if ladoA == ladoB and ladoB == ladoC:
        print(f"{msg} equilatero")
    elif ladoA != ladoB and ladoB != ladoC:
        print(f"{msg} escaleno")
    else:
        print(f"{msg} isosceles")

else:
    print("Los lados ingresados no conforman un triangulo")
