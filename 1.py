intentos = 0
while True:
    print('¿Quién eres?')
    nombre = input()
    intentos += 1
    if nombre != 'Abel':
        print('Intento {intentos}. Usuario incorrecto. Intenta de nuevo.')
        continue
    print('Hola, Abel, ¿cuál es tu contraseña?')
    contraseña = input()
    intentos += 1
    if contraseña != 'lol1234':
        print('Intento {intentos}. Contraseña incorrecta. Intenta de nuevo.')
        continue
    break
if intentos > 3:
    print('Acceso denegado. Demasiados intentos fallidos.')
else:
    print('Bienvenido, Abel!')