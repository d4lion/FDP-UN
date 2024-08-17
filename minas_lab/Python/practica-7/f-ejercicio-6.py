def sumar_digitos(numero: int):

    suma = 0

    # Separar los numeros en una lista invertida
    numero_separado = list(reversed(str(numero)))

    # Se transforma todos los trings en enteros
    numero_separado = list(map(lambda x: int(x), numero_separado))

    # Se elimina el numero de verificacion
    numero_separado.pop(0)

    for index, num in enumerate(numero_separado, start=1):
        if index % 2 == 0:
            suma += num
        else:
            suma += num * 3

    return suma


def verificar_codigo(suma_digitos):

    suma_digitos += 7

    if suma_digitos % 10 == 0:
        return "CORRECTO"

    return "INCORRECTO"


numero = int(input())

while numero != -1:
    print(verificar_codigo(sumar_digitos(numero)))
    numero = int(input())
