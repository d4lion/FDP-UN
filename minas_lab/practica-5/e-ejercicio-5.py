reprobadosIntegral: int = int(input())
reprobadosLineal: int = int(input())


def recolectarDatos(cantidad: int):
    listaAux: list = []

    while cantidad > 0:
        listaAux.append(int(input()))
        cantidad -= 1

    return listaAux


codigosIntegral: list = recolectarDatos(reprobadosIntegral)
codigosLineal: list = recolectarDatos(reprobadosLineal)

numeroMaterias: dict = {}
reprobadasAmbasMaterias: list = []



for codigoIntegral in codigosIntegral:
    if codigoIntegral not in numeroMaterias:
        numeroMaterias[codigoIntegral] = 1

for codigoLineal in codigosLineal:
    if codigoLineal in numeroMaterias:
        numeroMaterias[codigoLineal] += 1

for clave, valor in numeroMaterias.items():
    if valor == 2:
        reprobadasAmbasMaterias.append(clave)

print("Los estudiantes que reprobaron ambas materias son:", *reprobadasAmbasMaterias)
