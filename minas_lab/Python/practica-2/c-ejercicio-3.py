numero_1 = int(input())
numero_2 = int(input())


def multiplos(n1, n2):
    if (n1 % 117 == 0):
        return f"Los numeros {n1} y {n2} tienen al planeta condenado, bien condenado"
    elif (n1 % 127 == 0):
        return f"Los numeros {n1} y {n2} tienen al planeta condenado, bien condenado"
    elif (n2 % 117 == 0):
        return f"Los numeros {n1} y {n2} tienen al planeta condenado, bien condenado"
    elif (n2 % 127 == 0):
        return f"Los numeros {n1} y {n2} tienen al planeta condenado, bien condenado"

    return f"Los numeros {n1} y {n2} han salvado al planeta"


print(multiplos(numero_1, numero_2))
