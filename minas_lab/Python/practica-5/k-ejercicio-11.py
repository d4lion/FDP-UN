lista: list[int] = [i for i in range(1, 6)]

finLista: int = len(lista) - 1
inicio: int = 0

while finLista > inicio:
    lista[finLista], lista[inicio] = lista[inicio], lista[finLista]
    finLista -= 1
    inicio += 1

print(lista)