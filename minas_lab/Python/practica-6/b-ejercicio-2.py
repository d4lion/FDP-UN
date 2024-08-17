from typing import Union


def fibonacci(cantidad: int) -> list:
    fib_list = []
    anterior = 0
    actual = 0

    for i in range(0, cantidad):

        if len(fib_list) == 0:
            fib_list.append(i)
            continue
        elif len(fib_list) == 1:
            fib_list.append(i)
            actual = 1
            continue

        cantidad_actual = fib_list[actual]
        cantidad_anterior = fib_list[anterior]

        fib_list.append(cantidad_actual + cantidad_anterior)

        anterior += 1
        actual += 1

    return fib_list


def fibSecond(cantidad: int) -> Union[str, None]:

    anterior = 0
    actual = 1

    while cantidad > 0:
        print(anterior)

        aux = anterior + actual
        anterior = actual
        actual = aux

        cantidad -= 1


fibSecond(12)
