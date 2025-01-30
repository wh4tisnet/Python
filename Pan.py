pan_blanco = int(input("¿Cuántas unidades de pan blanco quieres?: "))
pan_integral = int(input("¿Cuántas unidades de pan integral quieres?: "))

if pan_blanco < 0:
    print("No puedes introducir cantidades negativas.")
elif pan_integral < 0:
    print("No puedes introducir cantidades negativas.")
else:
    precio_pan_blanco = pan_blanco * 1.00
    precio_pan_integral = pan_integral * 1.50
    precio_total = precio_pan_blanco + precio_pan_integral

    if pan_blanco >= 10:
        precio_pan_blanco -= 1
    if pan_integral >= 10:
        precio_pan_integral -= 1

    precio_total = precio_pan_blanco + precio_pan_integral

    print(f"El total a pagar es: {precio_total:.2f} €")

    pago = float(input("¿Cuánto dinero entrega?: "))
    if pago < precio_total:
        print(f"Faltan {precio_total - pago:.2f} €")
    else:
        print(f"El cambio es de: {pago - precio_total:.2f} €")
