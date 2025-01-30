print('NOTAS')
nota = float(input("Introduce tu nota: "))

if nota < 5:
    print('Insuficiente', nota)
elif nota == 5:
    print('Suficiente', nota)
elif nota == 6:
    print('Bien', nota)
elif 7 <= nota <= 8:
    print('Notable', nota)
elif 9 <= nota <= 10:
    print('Sobresaliente', nota)
else:
    print('Nota no válida')
