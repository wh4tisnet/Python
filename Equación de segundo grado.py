import math

print("Ecuación de segundo grado")
a = float(input('Dame el valor del coeficiente a: '))
b = float(input('Dame el valor del coeficiente b: '))
c = float(input('Dame el valor del coeficiente c: '))

d = b**2 - 4*a*c

if d < 0:
    print("Esta ecuación no tiene soluciones reales.")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print(f"El primer número: x1 = {x1}")
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"El segundo número: x2 = {x2}")
