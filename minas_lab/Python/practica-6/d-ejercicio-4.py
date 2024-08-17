def numeroPerfecto(num: int):
    if num < 0:
        return

    divisores = []

    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)

    if sum(divisores) == num:
        return True

    return False


cantidadDeCasos = int(input())


for i in range(cantidadDeCasos):
    numero = int(input())
    esNumeroPerfecto = numeroPerfecto(numero)

    if (esNumeroPerfecto):
        print(f'El numero {numero} es perfecto')
    else:
        print(f'El numero {numero} no es perfecto')
