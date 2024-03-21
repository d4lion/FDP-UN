cantidadDeBacterias: float = float(input())
horas: int = 0


while cantidadDeBacterias >= 10:
    cantidadDeBacterias = cantidadDeBacterias / 2
    horas += 1

print(horas)