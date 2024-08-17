

def functionTramos(num: int) -> int:
    if num >= 2:
        return num + 3

    return num**2 - 7 * num + 5


cantidadDeCasos = int(input())

for i in range(cantidadDeCasos):
    print(functionTramos(int(input())))
