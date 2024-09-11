print("--------------------")
print("*** Calificador ****")
print("--------------------")
cual=input("Quieres calificar alumnos? s para si o n para no \n")
while cual=="s":
    nota=int(input("Nota del alumno: "))
    if nota>4:
        print("El alumnos esta aprobado")
    else:
        print("El alumnos no esta aprobado")
    cual=input("Quiere continuar? ")
    if cual=="n":
        print("")
