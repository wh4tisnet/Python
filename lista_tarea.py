nombre = input("Por favor introduzca su nombre: ")
print(f"Es un gusto, {nombre}")
print("Déjame presentarme, yo soy Mat y soy un mini programa informático que te ayudará con tus tareas a lo largo del día.")

tareas = []

for i in range(1, 7):
    tarea = input(f"Por favor dime la tarea {i}: ")
    tareas.append(tarea)

print("Entendido señor, sus tareas son:", ", ".join(tareas))

while True:
    continuar = input("¿Quiere añadir más tareas? (s para sí, n para no): ").lower()
    if continuar == 'n':
        break
    tarea = input("Por favor, introduzca la nueva tarea: ")
    tareas.append(tarea)

print("Ahora su lista completa de tareas es:", ", ".join(tareas))
print("Señor, ¿está seguro de que no necesita nada más?")
print("Estoy aquí para servirle señor, si necesita algo más no dude en solicitar mi ayuda.")

with open("lista_tareas.txt", "w") as file:
    file.write("\n".join(tareas))

print("Su lista de tareas ha sido guardada en 'lista_tareas.txt'.")
