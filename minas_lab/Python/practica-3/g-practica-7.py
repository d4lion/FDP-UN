"""
QUE ESTACION DEL AÑO ES

drive = https://drive.google.com/file/d/1HntKNhGi3X33SLiQILLjOiF6cgsNb9ln/view?usp=sharing

"""


nombreMes: str = input()
diaMes: int = int(input())

primaveraListaMeses = ["Marzo", "Abril", "Mayo"]
veranoListaMeses = ["Junio", "Julio", "Agosto", "Septiembre"]
otonoListaMeses = ["Septiembre", "Octubre", "Noviembre", "Diciembre"]

if nombreMes in primaveraListaMeses and diaMes >= 20 and diaMes <= 31:
    print("Primavera")
elif nombreMes in veranoListaMeses and diaMes >= 1 and diaMes <= 21:
    print("Verano")
elif nombreMes in otonoListaMeses and diaMes >= 1 and diaMes <= 22:
    print("Otono")
else:
    print("Invierno")
