"""

En el ejercicio anterior se recordó la definición de número primo, en este caso vamos a trabajar con
números compuestos, ¿recuerdas su definición?, pues es muy sencilla, un número es compuesto
cuando no es primo.
Mejor elabora un programa que reciba una cantidad N
de números ingresados por el usuario, al final, el programa deberá imprimir el promedio de los
números compuestos que se ingresaron.

"""

cantidadNumeros: int = int(input())

totalCompuestos: int = 0
cantidadCompuestos: int = 0

for i in range(0, cantidadNumeros):
    numero: int = int(input())
    divisores: int = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores += 1

    if divisores > 2:
        totalCompuestos += numero
        cantidadCompuestos += 1

print(round(totalCompuestos / cantidadCompuestos, 1))
