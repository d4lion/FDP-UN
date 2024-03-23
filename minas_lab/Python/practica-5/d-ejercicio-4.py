numeroDeNotas: int = int(input())

notas: list = []
notasAltoPromedio: list = []
notasBajoPromedio: list = []

for i in range(0, numeroDeNotas):
    nota: float = float(input())
    notas.append(nota)

promedioDeNotas: float = round(sum(notas) / numeroDeNotas, 1)


for indexNota in range(0, len(notas)):
    notaActual = notas[indexNota]

    if notaActual < promedioDeNotas:
        notasBajoPromedio.append(notaActual)
    else:
        notasAltoPromedio.append(notaActual)

print(*notasAltoPromedio)
print(*notasBajoPromedio)
