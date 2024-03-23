"""
-------------------------------- CAPACIDAD DE CARGA -------------------------------------------

En la plaza de mercado de la ciudad se dispone de un camión con una capacidad de carga
determinada por las características del fabricante. El almacén «Abarrotes El Vecino» necesita
transportar una carga de papa capira hacia un municipio aledaño. La carga de papa capira está
distribuida en múltiples bultos o sacos de tamaño y peso variable. El asunto es que, para poder
comenzar a negociar con el transportador, se necesita primero determinar cuántos bultos de papa
caben en el camión sin que se exceda su capacidad de carga. ¿Harías un programa que ayude a
determinar cuántos bultos o sacos de papa caben en el camión sin exceder la capacidad de carga de
este?

"""

capacidadMaxCamion: float = float(input())
cantidadDeBultos: int = int(input())
bultosTotales: int = 0

for i in range(0, cantidadDeBultos):
    pesoBulto: int = int(input())

    if capacidadMaxCamion >= 0:
        capacidadMaxCamion -= pesoBulto

        if not capacidadMaxCamion < 0:
            bultosTotales += 1

print(f"Caben {bultosTotales} bultos de papa")