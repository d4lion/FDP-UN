"""
ECUACIÓN GENERAL

drive = https://drive.google.com/file/d/1eXSymiRSS6Q3Q_9EKffwzN-69ZG3h_sQ/view

Resumen
Determinar si tiene soluciones reales de ser así
mostrar cuales son esas soluciones
"""

from math import pow, sqrt

a: float = float(input())
b: float = float(input())
c: float = float(input())

discriminante = pow(b, 2) - (4 * a * c)


def bascara(a, b, discriminante):
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)

    return round(x1, 1), round(x2, 1)


if discriminante > 0:
    mensaje: str = "La ecuacion tiene dos soluciones reales, ellas son"
    x1, x2 = bascara(a, b, discriminante)
    print(f"{mensaje} X1 = {x1} y X2 = {x2}")
elif discriminante == 0:
    mensaje: str = "La ecuacion tiene una solucion real, ella es"
    print(f"{mensaje} X = {bascara(a, b, discriminante)[0]}")
else:
    print("La ecuacion no tiene solucion en los reales")
