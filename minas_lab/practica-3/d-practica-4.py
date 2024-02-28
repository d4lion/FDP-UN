"""
DE QUE COLOR ES EL CUADRADO

drive = https://drive.google.com/file/d/176ReL7XHIVoPXfHEPJLhe3MPOpKs4SOM/view

"""

numeroDeFila: int = int(input())
numeroDeColumna: int = int(input())

if numeroDeFila % 2 != 0:
    if numeroDeColumna % 2 == 0:
        print("BLANCO")
    else:
        print("NEGRO")
else:
    if numeroDeColumna % 2 == 0:
        print("NEGRO")
    else:
        print("BLANCO")
