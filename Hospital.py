nombre = input("Nombre: ")

presupuesto = float(input("Introduce el presupuesto para el hospital: "))

presupuesto_ginecologia = presupuesto * 0.50
presupuesto_pediatria = presupuesto * 0.30
presupuesto_traumatologia = presupuesto * 0.20

print(f"El presupuesto para Ginecología es: {presupuesto_ginecologia}")
print(f"El presupuesto para Pediatría es: {presupuesto_pediatria}")
print(f"El presupuesto para Traumatología es: {presupuesto_traumatologia}")
