def almacenar_palabras(palabras: str):
    global traduccion_de_palabras

    palabras = palabras.split(":")

    traduccion_de_palabras[palabras[0]] = palabras[1]


traduccion_de_palabras: dict[str, str] = {}

cantidad_de_palabras = int(input())

for i in range(cantidad_de_palabras):
    palabra = input()
    almacenar_palabras(palabra)

cantidad_de_frases_a_traducir = int(input())

frases: list[str] = []

for j in range(cantidad_de_frases_a_traducir):
    frase = input().split(" ")
    frase_traducida = ""

    for palabra in frase:
        traduccion = traduccion_de_palabras.get(palabra)
        frase_traducida += f"{traduccion} "

    frases.append(frase_traducida)

print(*frases, sep="\n")