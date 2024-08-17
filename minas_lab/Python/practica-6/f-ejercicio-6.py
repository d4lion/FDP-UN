from typing import Union
from math import pow, sqrt


def f(x: int) -> Union[float, int]:
    if x > 3:
        return pow(x, 2) - (6*x) + 4

    if 3 >= x > -1:
        return pow(x, 3) + 8

    if x <= -1:
        return sqrt(x + 8)


def g(x: int) -> Union[float, int]:
    return 3 - x


entrada = float(input())

print(round(f(g(entrada)), 1))
print(round(g(f(entrada)), 1))
print(round(f(f(entrada)), 1))
print(round(g(g(entrada)), 1))
