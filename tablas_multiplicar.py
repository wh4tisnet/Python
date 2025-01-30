def tabla_multiplicar_for(numero):
    print(f"Tabla de multiplicar del {numero} (usando for):")
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")

def tabla_multiplicar_while(numero):
    print(f"\nTabla de multiplicar del {numero} (usando while):")
    i = 1
    while i <= 10:
        print(f"{i} x {numero} = {i * numero}")
        i += 1

def main():
    numero = int(input("Introduce un número: "))
    tabla_multiplicar_for(numero)
    print("\n" + "="*30 + "\n")
    tabla_multiplicar_while(numero)

if __name__ == "__main__":
    main()
