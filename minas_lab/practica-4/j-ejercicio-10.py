numero: str = input()
mayor: int = 0
menor: int = 9999


for digito in numero:
    digito = int(digito)
    if digito > mayor:
        mayor = digito
    elif digito < menor:
        menor = digito

print(mayor - menor)