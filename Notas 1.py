print('Notas')
nota = float(input('Introduce la nota: ').replace (',','.'))
if nota <=4:
    print('Insuficiente', nota)
elif nota ==5:
    print('Suficiente', nota)
elif nota ==6:
    print('Bien', nota)
elif 7<= nota <=8:
    print('Notable', nota)
elif 9<= nota <=10:
    print('Sobresaliente', nota)