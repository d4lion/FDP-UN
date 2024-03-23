cantidadDorsales: int = int(input())

totalDorsale: set = set(i for i in range(1, cantidadDorsales + 1))
dorsalesIngresadas: list = []

while cantidadDorsales > 1:
    dorsalesIngresadas.append(int(input()))
    cantidadDorsales -= 1

print(f"La dorsal que falta es:", *list(totalDorsale.difference(dorsalesIngresadas)))
