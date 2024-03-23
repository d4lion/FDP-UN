"Conteo de partidas"

numeroDePartidas: int = int(input(""))
intervaloInferior: int = int(input(""))
intervaloSuperior: int = int(input(""))

partidas: list = []
repeticiones: dict = {}

# Inicializamos los intervalos en el diccionario
for x in range(intervaloInferior, intervaloSuperior + 1):
    repeticiones[x] = 0

# Agregamos los datos de las partidas
while numeroDePartidas > 0:

    partida: int = int(input(""))

    # Filtramos los datos que van en el intervalo
    if partida in repeticiones:
        partidas.append(partida)
    numeroDePartidas -= 1


# Inicializar las variables del diccionario
for partida in partidas:
    repeticiones[partida] += 1

# Imprimomos en pantalla los datos
[print(f"{clave}: {valor}") for clave, valor in repeticiones.items()]
