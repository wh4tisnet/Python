print("==========================")
print("***    CALCULADORA     ***")
print("==========================")
x = int(input("Primer numero: "))
s = input("Operacion: ")
y = int(input("Segundo numero: "))
if s=="+" or s=="-" or s=="*" or s=="/":
    if s == "+":
        print("El resultado de",x,"+",y,"es igual a:" ,x + y)
    elif s == "-":
        print("El resultado de",x,"-",y,"es igual a:" ,x - y)
    elif s == "*":
        print("El resultado de",x,"*",y,"es igual a:" ,x * y)
    elif s == "/":
        print("El resultado de",x,"/",y,"es igual a:" ,x / y)
else:
    print("Esta operacion no es valida")