while True:
    print("\n1. saludar\n2. despedirse\n3. salir")
    opcion = input("elige una opcion: ")
    if opcion == "1":
        print("hola")
    elif opcion == "2":
        print("adios")
    elif opcion == "3":
        print("saliendo del menu ")
        break
    else:
        print("opcion no valida")