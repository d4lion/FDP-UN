"Recta numerica"

cantidadDeElementos: int = int(input())
elementos: list = []

while cantidadDeElementos > 0:
    elementos.append(int(input("")))
    cantidadDeElementos -= 1


for i in range(0, len(elementos)):
    for j in range(0, len(elementos)):
        if elementos[j] > elementos[i]:
            elementos[j], elementos[i] = elementos[i], elementos[j]

print(elementos)