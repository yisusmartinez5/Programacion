while True:
    contraseña = input("introduce una contraseña segura (minima de 8 caracteres) ")
    if len(contraseña) >= 8:
        print("contraseña segura registrada ")
        break
    else:
        print("error: la contraseña debe tener minimo 8 caracteres")