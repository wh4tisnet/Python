def es_par_o_impar(numero):
    return "par" if numero % 2 == 0 else "impar"

numero = int(input("Introduce un número: "))

resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}.")
