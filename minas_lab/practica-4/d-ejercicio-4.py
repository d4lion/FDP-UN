cantidadDeCuadrados: int = int(input())
variacionDeL: float = 0
AreaTotal: float = 0

for i in range(0, cantidadDeCuadrados):
    L: float = float(input())
    variacionDeL = L + variacionDeL
    AreaTotal += variacionDeL**2

print(f"Ramon, el area total de la estructura basica del universo es de {AreaTotal} centimetros cuadrados")



