def f(x: int) -> int:
    return x**2 + (5*x) - 3


def g(x: int) -> int:
    return x + 1


entrada = int(input())

print(f(g(entrada)))
print(g(f(entrada)))
print(f(f(entrada)))
