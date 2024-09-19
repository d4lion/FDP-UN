def contar_verbos_participio(verbos: list[str]) -> int:
    contador = 0

    for verbo in verbos:
        if verbo.endswith("ado") or verbo.endswith("ido"):
            contador += 1

    return contador


numero_casos = int(input())

for i in range(numero_casos):
    # La entrada debe verse así: "comido*bebido*ido*jugado"
    entrada_verbos = input().split("*")

    print(contar_verbos_participio(entrada_verbos))