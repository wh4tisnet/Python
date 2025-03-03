intentos = 0
max_intentos = 3

while intentos < max_intentos:
    nombre = input('¿Quién eres? ')
    intentos += 1
    if nombre != 'Abel':
        print(f'Intento {intentos}. Usuario incorrecto. Intenta de nuevo.')
        continue

    contraseña = input('Hola, Abel, ¿cuál es tu contraseña? ')
    intentos += 1
    if contraseña != 'lol1234':
        print(f'Intento {intentos}. Contraseña incorrecta. Intenta de nuevo.')
        continue

    print('Bienvenido, Abel!')
    break
else:
    print('Acceso denegado. Demasiados intentos fallidos.')
