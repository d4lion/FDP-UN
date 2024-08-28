def obtenerOrigen(terminacion: str):
    terminaciones: dict = {
        "ix": "Galo",
        "us": "Romano",
        "ic": "Godo",
        "as": "Griego",
        "af": "Normando",
        "is": "Breton",
        "ez": "Hispano",
    }

    return terminaciones.get(terminacion, "Desconocido")


cantidad_de_datos = int(input())

while True:

    if cantidad_de_datos == 0:
        break

    cantidad_de_datos -= 1

    nombre = input()

    if (nombre[-1]) == "a":
        print("Indio")
    else:
        print(obtenerOrigen(f"{nombre[-2]}{nombre[-1]}"))
