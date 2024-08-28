def esPanvocalica(palabra: str):

    palabra = palabra.lower()
    vocales_usadas = []

    vocales = ['a', 'e', 'i', 'o', 'u']

    for letra in palabra:
        if letra in vocales:
            vocales_usadas.append(letra)

    # Impide que se repitan las letras
    vocales_usadas = set(vocales_usadas)

    if len(vocales_usadas) == 5:
        return True
    else:
        return False


cantidad_casos = int(input())

while True:

    if cantidad_casos == 0:
        break

    cantidad_casos -= 1

    palabra = input()

    if esPanvocalica(palabra):
        print("Panvocalica")
    else:
        print("No panvocalica")
