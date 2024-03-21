"""
TABLA DE MULTIPLICAR

drive = https://drive.google.com/file/d/1Qa1wCK7-PuSpt9XrDObp-_UoZ9bTwNWC/view

Resumen
Hacer las tablas de multiplicar de un dato m hasta un dato n
"""

num: int = int(input())
num_multiplos: int = int(input())

for i in range(1, num_multiplos + 1):
    print(f"{num} x {i} = {num * i}")