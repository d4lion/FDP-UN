"""
VELOCIDAD

drive = https://drive.google.com/file/d/1iAb1SIzIozvviaw8m5QZ0rqFsP6RswT0/view?usp=sharing
"""


valore_ingresados: dict[str, float] = {
    input().upper(): float(input()),
    input().upper(): float(input())
}


if "V" not in valore_ingresados:
    print(f"V = {valore_ingresados["D"] / valore_ingresados["T"]}")
elif "T" not in valore_ingresados:
    print(f"T = {valore_ingresados["D"] / valore_ingresados["V"] }")
else:
    print(f"D = {valore_ingresados["T"] * valore_ingresados['V']}")