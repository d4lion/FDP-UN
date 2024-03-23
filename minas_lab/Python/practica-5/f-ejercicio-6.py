totalEstampitas: int = int(input())

codigoEstampitas: list = []
repeticiones: dict = {}
estampitasPorCambiar: int = 0

while totalEstampitas > 0:
    codigo: int = int(input())
    codigoEstampitas.append(codigo)
    totalEstampitas -= 1

for codigo in codigoEstampitas:
    if codigo not in repeticiones:
        repeticiones[codigo] = 0
    else:
        repeticiones[codigo] += 1

for codigo, repeticiones in repeticiones.items():
    if repeticiones > 0:
        estampitasPorCambiar += repeticiones

print(f"Carlitos debe intercambiar {estampitasPorCambiar} estampitas para no tener repeticiones")
