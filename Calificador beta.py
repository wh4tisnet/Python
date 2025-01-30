print("Calificador")
cual = input("¿Quieres calificar alumnos? (s para sí o n para no) \n").lower()

while cual == "s":
    nota = int(input("Nota del alumno: "))
    if nota > 4:
        print("2")
    else:
        print("3")
    
    cual = input("¿Quieres continuar? (s para sí o n para no) \n").lower()

print("Programa terminado.")
