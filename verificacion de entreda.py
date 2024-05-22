while True:
    entrada = input("introduce un numero entero ")
    if entrada.isdigit():
        numero = int(entrada)
        print(f"el numero entero es {numero}")
        break
    else:
        print("error: entrada no valida, introduce un numero valido ")