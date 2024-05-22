while True:
    email = input("introduce tu email: ")
    if "@jesus.mx" in email and "." in email:
        print("email valido")
        break
    else:
        print("email no valido, intenta de nuevo")