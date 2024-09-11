print("--------------------")
print("*** Calificador ****")
print("--------------------")
cual=input("Quieres calificar alumnos? s para si o n para no \n")
while cual=="s":
    nota=int(input("Nota del alumno: "))
    if nota>4:
        print("2")
    else:
        print("3")
    cual=input("Quiere continuar? ")
