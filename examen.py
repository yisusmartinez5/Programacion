print("menu de la cafeteria")
print("¿Que deseas ordenar? ")
while True:
    print("\n1. bebidas\n2. comida\n3. postre\n4. Finalizar orden ")
    opcion = input("elige una opcion: ")
    if opcion == "1":
        print("tenemos las siguientes bebidas el dia de hoy:")
        print("\n1. Agua de jamaica\n2. Agua de horchata\n3. Agua de limon\n4. Agua de sandia\n5. coca cola\n6. delawer ponch\n7. fresca\n8. sprite\n9. pepsi\n10. Agua natural")
        bebidas = input("elige una opcion: ")
        if bebidas == "1":
             tamaño = input("Has elejido agua de jamaica ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50
        elif bebidas == "2":
             tamaño = input("Has elejido agua de horchata ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50  
        elif bebidas == "3":
             tamaño = input("Has elejido agua de limon ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50 
        elif bebidas == "4":
             tamaño = input("Has elejido agua de sandia ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50     
        elif bebidas == '5':
             tamaño = input("Has elejido coca ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 19
             else:
                 litro = 27 
        elif bebidas == '6':
             tamaño = input(" Has elejido delawer ponch ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24
        elif bebidas == '7':
             tamaño = input(" Has elejido fresca ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24  
        elif bebidas == '8':
             tamaño = input(" Has elejido sprite ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24 
        elif bebidas == '9':
             tamaño = input(" Has elijido pepsi ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 17
             else:
                 litro = 25
        else:
            input(" Has elijido Agua natural ¿Que tamaño deseas ingresar?: medio litro o litro")
            if tamaño == 'medio litro':
                 medio_litro = 10
            else:
                 litro = 15  
    elif opcion == "2":
        print("tenemos las siguientes comidas el dia de hoy:")
        print("\n1. Agua de jamaica\n2. Agua de horchata\n3. Agua de limon\n4. Agua de sandia\n5. coca cola\n6. delawer ponch\n7. fresca\n8. sprite\n9. pepsi\n10. Agua natural")
        bebidas = input("elige una opcion: ")
        if bebidas == "1":
             tamaño = input("Has elejido agua de jamaica ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50
        elif bebidas == "2":
             tamaño = input("Has elejido agua de horchata ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50  
        elif bebidas == "3":
             tamaño = input("Has elejido agua de limon ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50 
        elif bebidas == "4":
             tamaño = input("Has elejido agua de sandia ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 25
             else:
                 litro = 50     
        elif bebidas == '5':
             tamaño = input("Has elejido coca ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 19
             else:
                 litro = 27 
        elif bebidas == '6':
             tamaño = input(" Has elejido delawer ponch ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24
        elif bebidas == '7':
             tamaño = input(" Has elejido fresca ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24  
        elif bebidas == '8':
             tamaño = input(" Has elejido sprite ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 16
             else:
                 litro = 24 
        elif bebidas == '9':
             tamaño = input(" Has elijido pepsi ¿Que tamaño deseas ingresar?: medio litro o litro")
             if tamaño == 'medio litro':
                 medio_litro = 17
             else:
                 litro = 25
        else:
            input(" Has elijido Agua natural ¿Que tamaño deseas ingresar?: medio litro o litro")
            if tamaño == 'medio litro':
                 medio_litro = 10
            else:
                 litro = 15  
    elif opcion == "3":
        print("saliendo del menu ")
        break
    else:
        print("opcion no valida")   