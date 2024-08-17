from math import factorial

def taylor(cantidad_terminos: int, radianes: float):
    aproximacion_coseno = 0
    resultados = []
    
    # Posicion, siempre se empieza por el segundo termino
    exponente = 0


    for termino_actual in range(1, cantidad_terminos + 1):
        if termino_actual == 1:
            aproximacion_coseno += 1
            resultados.append(termino_actual)
            exponente += 2
        elif termino_actual % 2 == 0:
            operation = -radianes**exponente / factorial(exponente)
            aproximacion_coseno += operation
            resultados.append(operation)
            termino_actual += 1
            exponente += 2
        else:
            operation = radianes**exponente / factorial(exponente)
            aproximacion_coseno += operation
            resultados.append(operation)
            termino_actual += 1
            exponente += 2


    return [aproximacion_coseno, resultados]

cantidad_de_terminos = int(input())
radianes = float(input())

res_aproximacion, ls_resultados = taylor(cantidad_de_terminos, radianes)

ls_resultados = list(map(lambda x: round(x, 2), ls_resultados))


print(*ls_resultados, sep=', ')
print(round(res_aproximacion, 2))