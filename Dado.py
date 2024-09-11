from random import randint
while True:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado3 = randint(1, 6)
    print("dado1", str(dado1))
    print("dado2", str(dado2))
    print("dado3", str(dado3))
    if dado1 == 6 and dado2 == 6 and dado3 == 6:
        print("Excelente")
        break
    elif (dado1 == 6 and dado2 == 6) or (dado2 == 6 and dado3 == 6) or (dado1 == 6 and dado3 == 6):
        print("Muy bien")
        break
    elif dado1 == 6 or dado2 == 6 or dado3 == 6:
        print("Regular")
    else:
        print("Pesimo")