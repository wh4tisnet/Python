import math

print("===============================================")
print("***  Calculadora de equaciones de 2º grado  ***")
print("===============================================")

valorA=eval(input("Intorduce el valor de 'a':"))
valorB=eval(input("Intorduce el valor de 'b':"))
valorC=eval(input("Intorduce el valor de 'c':"))

ValorBquadrat=valorB**2    # b^2
Valor4AC=4*valorA*valorC   # 4·a·c
Valor2A=2*valorA           # 2·a

valorX1=(-valorB+math.sqrt(ValorBquadrat-Valor4AC))/Valor2A
valorX2=(-valorB-math.sqrt(ValorBquadrat-Valor4AC))/Valor2A
print("Valor X1= ", valorX1)
print("Valor X2= ", valorX2)