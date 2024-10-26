print("CALCULADORA")
num1 = int(input("Primer numero: "))
oper = input("Operacion: ")
num2 = int(input("Segundo numero: "))
if oper=="+" or oper=="-" or oper=="*" or oper=="/":
    if oper == "+":
        print("El resultado de la suma es igual a:" num1 + num2)
    elif s == "-":
        print("El resultado de la resta es igual a:" num1 - num2)
    elif s == "*":
        print("El resultado de la multiplicación es igual a:" num1 * num2)
    elif s == "/":
        print("El resultado de la division es igual a:" num1 / num2)
else:
    print("Esta operacion no es valida")
