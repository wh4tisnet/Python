#identificador de numeros pares/impares
n=input("Escribe un numero: ")
n=eval(n)
if n%2==0:
    div2=n/2
    print("El numero",n,"es divisible por 2")
    print("Al dividir",n,"entre 2 se obtiene",div2)
elif n%3==0:
    div3=n/3
    print("El numero",n,"es divisible por 3")
    print("Al dividir",n,"entre 3 se obtiene",div3)
elif n%5==0:
    div5=n/5
    print("El numero",n,"es divisible por 5")
    print("Al dividir",n,"entre 5 se obtiene",div5)
elif n%7==0:
    div7=n/7
    print("El numero",n,"es divisible por 7")
    print("Al dividir",n,"entre 7 se obtiene",div7)
elif n%11==0:
    div11=n/11
    print("El numero",n,"es divisible por 11")
    print("Al dividir",n,"entre 11 se obtiene",div11)
elif n%13==0:
    div13=n/13
    print("El numero",n,"es divisible por 13")
    print("Al dividir",n,"entre 13 se obtiene",div13)