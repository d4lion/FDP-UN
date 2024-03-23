from math import floor

numeroDeNotas: int = int(input(""))

notas1: list[float] = []
notas2: list[float] = []
casos: list[int] = []

for i in range(1, (numeroDeNotas * 2) + 1):

    # Rellenar primera lista
    if i <= numeroDeNotas:
        notas1.append(float(input("")))
    else:
        notas2.append(float(input("")))

# Calcular las veces que se repiten los casos
for index in range(0, len(notas1)):
    if notas1[index] > notas2[index]:
        casos.append(1)
    elif notas1[index] < notas2[index]:
        casos.append(2)
    else:
        casos.append(0)

# Imprimir en pantalla lo faltante
print(notas1)
print(casos)
print(notas2)

print(f"Gana 1: {floor((casos.count(1) * 100) / numeroDeNotas)}")
print(casos.count(1))
print(f"Gana 2: {round((casos.count(2) * 100) / numeroDeNotas, 1)}")
print(casos.count(2))
print(f"Igual: {round((casos.count(0) * 100) / numeroDeNotas, 1)}")
print(casos.count(0))
