"""
Se dice que un número natural es Guay, cuando es igual a la suma de una cierta cantidad de números
naturales consecutivos comenzando en 1. Así, por ejemplo, los números 1, 3, 6 y 10 son guays, ya
que:
1 = 1
3 = 1 + 2
6 = 1 + 2 + 3
10 = 1 + 2 + 3 + 4
"""


def guay(num: int) -> bool:
    acomulaciones = 0
    for i in range(1, num + 1):
        acomulaciones += i

        if acomulaciones == num:
            return 'Numero guay'

    return 'Numero no guay'


number = int(input(''))
print(guay(number))
