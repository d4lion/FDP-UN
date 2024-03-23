"""
------------------------------------ INVERTIR NÚMERO ----------------------------------------

Escriba un programa para que, dado un número entero mayor a 9, se muestre en orden inverso. Por
ejemplo, si el número es 8351, el programa debe mostrar 1538.
"""


numero: str = input()
salida: str = ""
longituNumero: int = len(numero)

for i in range(0, longituNumero):
    salida += numero[longituNumero-(i+1)]

print(salida)

## PARA UNA SOLUCION MAS SENCILLA
print(numero[::-1])