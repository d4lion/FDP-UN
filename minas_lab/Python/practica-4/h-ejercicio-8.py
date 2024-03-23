"""
--------------------------- NÚMEROS PRIMOS --------------------------------------------
¿Recuerdas la definición matemática de número primo?, por si acaso, aquí va de nuevo:
Un número primo es aquel que solamente tiene dos divisores, el mismo número y el uno, así, por
ejemplo, valores como el 2, el 3 o el 5 se consideran números primos, ya que solamente son divisibles
por sí mismos y por la unidad.

"""

cantidadNumeros: int = int(input())

totalPrimos: int = 0

for i in range(0, cantidadNumeros):
    numero: int = int(input())
    divisores: int = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores += 1

    if divisores == 2:
        totalPrimos += 1

print(totalPrimos)
