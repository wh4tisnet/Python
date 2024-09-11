nombre= str(input("Introduce tu nombre: "))
contra=str(input("Introduce tu contraseña: "))
if nombre == "admin" and contra == "password":
    print("Acceso al sistema")
else:
    if nombre == "admin" and contra== "1234":
        print("Esa contraseña no es de un admin")
    else:
        print("Acceso denegado")