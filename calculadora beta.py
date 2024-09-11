op1=eval(input("Introduce el primer operador: "))
operacion=input("Tipo de operacion: ")
op2=eval(input("Introduce el segundo operador: "))
if operacion=="+":
    suma=op1+op2
    print("el resultado es: ",suma)
if operacion=="-":
    resta=op1-op2
    print("El resultado es: ",resta)
if operacion=="*":
    mult=op1*op2
    print("El resultado es: ",mult)
if operacion=="/":
    div=op1/op2
    print("El resultado es: ",div)

    