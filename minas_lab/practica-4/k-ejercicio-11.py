"""
PATRON DE IMPRESIÓN

Escriba un programa para que dado un número de líneas L, se imprima el patrón que se indica a
continuación. Siendo L un número entero mayor o igual a 3 y siempre un número impar. Por ejemplo,
si L = 11 se debe imprimir el siguiente patrón. Note que el patrón imprime 11 líneas.

                                        *
                                        **
                                        ***
                                        ****
                                        *****
                                        ******
                                        *****
                                        ****
                                        ***
                                        **
                                        *
"""

numero: int = int(input())

if numero % 2 == 1 and numero >= 3:
    for i in range(1, (numero // 2) + 2):
        print("*" * i)

    for j in range((numero // 2) + 1, 1, -1):
        print("*" * (j - 1))

