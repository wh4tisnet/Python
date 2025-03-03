cantidad_pan = int(input("¿Cuántas unidades de pan quieres?: "))
precio_pan = 1.00
if cantidad_pan < 0:
    print("No puedes introducir cantidades negativas.")
else:
    total_pan = cantidad_pan * precio_pan - (1 if cantidad_pan >= 10 else 0)
    precio_total = total_pan
    agregar_agua = input("¿También deseas una botella de agua? (sí/no): ")
    if agregar_agua == "sí":
        cantidad_agua = int(input("¿Cuántas botellas de agua quieres?: "))
        precio_agua = 0.50
        if cantidad_agua < 0:
            print("No puedes introducir cantidades negativas.")
        else:
            total_agua = cantidad_agua * precio_agua - (1 if cantidad_agua >= 10 else 0)
            precio_total += total_agua
            print(f"Total a pagar: {precio_total:.2f} €")
    elif agregar_agua == "no":
        print(f"Total a pagar solo por el pan: {precio_total:.2f} €")
    else:
        print("Respuesta no válida. Por favor, escribe 'sí' o 'no'.")
    pago = float(input("¿Cuánto dinero entrega?: "))
    if pago < precio_total:
        print(f"Faltan {precio_total - pago:.2f} €")
    else:
        print(f"El cambio es de: {pago - precio_total:.2f} €")
