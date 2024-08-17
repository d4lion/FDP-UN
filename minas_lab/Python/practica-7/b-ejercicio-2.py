def narcisista(n):
    aux = n
    n = list(str(n))
    num_digitos = len(n)

    res_narcisista = list(map(lambda digito: int(digito)**num_digitos, n))
    
    if aux == sum(res_narcisista):
        return 1

    return 0




print(narcisista(int(input())))