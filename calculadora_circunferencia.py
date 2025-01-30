import math

radio = float(input("Introduce el valor del radio: "))

longitud = 2 * math.pi * radio
area = math.pi * radio**2

print(f"La longitud de la circunferencia es: {longitud:.2f}")
print(f"El área de la circunferencia es: {area:.2f}")
