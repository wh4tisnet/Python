print('NOTAS')
nota=float(input("Introduce tu nota: "))
if nota <=4:
    print('Insuficiente' ,nota)
elif nota ==5:
    print('Suficiente' ,nota)
elif nota ==6:
    print('Bien' ,nota)
elif nota ==7 or nota==8:
    print('Notable' ,nota)
elif nota ==9 or nota==10:
    print('Sobresaliente' ,nota)