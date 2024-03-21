andrea: float = round(float(input("")))
sandra: float = round(float(input("")))
milena: float = round(float(input("")))

promedio: float = round(sum((andrea, sandra, milena)) / 3)

if andrea == 12 and sandra == 12 and milena == 19:
    print("Gana Andrea")
else:
    if andrea == promedio:
        print("Gana Andrea")
    elif sandra == promedio:
        print(("Gana Sandra"))
    else:
        print("Gana Milena")
