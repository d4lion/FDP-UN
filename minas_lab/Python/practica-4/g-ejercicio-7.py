"""
------------------------------------  LA SUCESION ---------------------------------------
En Matemáticas, es muy común que cuando nos dan ciertos términos de una sucesión, tengamos
que encontrar su forma general, de tal manera que describa el patrón o comportamiento que se
sigue en la secuencia. ¡Vaya que muchas de ellas nos dan dolor de cabeza!
Para este ejercicio debemos hacer algo similar, la idea es construir un programa que se encargue de
imprimir los primeros N números de la siguiente sucesión:


                                17 15 18 16 19 17 20 18 21...
"""
catidadNumerosSucesion: int = int(input())

primerNumero: int = 17
segundoNumero: int = 15
print(primerNumero)

for i in range(1, catidadNumerosSucesion):

    if not i % 2 == 0:
        print(segundoNumero)
        segundoNumero += 1
    else:
        primerNumero += 1
        print(primerNumero)

