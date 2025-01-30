print("Calificador")
cual = input("¿Quieres calificar alumnos? (s para sí o n para no) \n")

while cual.lower() == "s":
    nota = int(input("Nota del alumno: "))
    if nota >= 5:
        print("El alumno está aprobado")
    else:
        print("El alumno no está aprobado")
    
    cual = input("¿Quieres continuar? (s para sí o n para no) \n")

print("Programa terminado.")
