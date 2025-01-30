print("CALCULADORA")
num1 = int(input("Primer número: "))
oper = input("Operación (+, -, *, /): ")
num2 = int(input("Segundo número: "))

if oper in ["+", "-", "*", "/"]:
    if oper == "+":
        print("El resultado de la suma es igual a:", num1 + num2)
    elif oper == "-":
        print("El resultado de la resta es igual a:", num1 - num2)
    elif oper == "*":
        print("El resultado de la multiplicación es igual a:", num1 * num2)
    elif oper == "/":
        if num2 != 0:
            print("El resultado de la división es igual a:", num1 / num2)
        else:
            print("Error: División por cero no permitida.")
else:
    print("Esta operación no es válida")
