import math
print("Equación de segundo grado")
a = float(input('Dame el valor del coeficiente a: '))
b = float(input('Dame el valor del coeficiente b: '))
c = float(input('Dame el valor del coeficiente c: '))
d = b*b-4*a*c
if d <0:
    print("Esta equacio nose")
else:
    x1 = (-b+math.sqrt(d))/2*a
    print("El primer numero: x1 = " + str(x1))
    x2 = (-b-math.sqrt(d))/2*a
    print("El segundo numero: x2 = " + str(x2))