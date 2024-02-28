nota = int(input())


if nota <= 100:
    if nota < 40:
        print(f"El grado numerico {nota} corresponde al grado en letra F")

    elif nota < 60 and nota > 40:
        print(f"El grado numerico {nota} corresponde al grado en letra E")

    elif nota < 70 and nota >= 60:
        print(f"El grado numerico {nota} corresponde al grado en letra D")

    elif nota < 80 and nota >= 70:
        print(f"El grado numerico {nota} corresponde al grado en letra C")

    elif nota < 90 and nota >= 80:
        print(f"El grado numerico {nota} corresponde al grado en letra B")
    else:
        print(f"El grado numerico {nota} corresponde al grado en letra A")
else:
    print(f"El valor {nota} no es un grado numerico valido")
