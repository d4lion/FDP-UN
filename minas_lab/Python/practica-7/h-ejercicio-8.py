filas = int(input())
columnas = int(input())

controladora = 0

for i in range(1, filas + 1):
    controladora += 1
    print(f"{controladora}", end=" ")

    for j in range(0, columnas - 1):
        if j != columnas - 2:
            print(f"{controladora ** j}", end=" ")
        else:
            print(f"{controladora ** j}")
