#creacion de listas
frutas = ['manzana', 'banana','cereza' ] # lista de tres elementos
    
while True:
        print(frutas)
        print("\nMenú de opciones:")
        print("\n1. imprimir el primero de lal lista\n2. cambiar el segundo \n3. agregar una nueva fruta\n4. remover una fruta\n5. Salir.")
        try:
            opcion = int(input("Elige una opción :) o presiona 5 para salir: "))
            if opcion == 1:
               #acceso a elementos
                print(frutas[0])#accediendo al primer elemento 
            elif opcion == 2:
                numero = input(print("que nunmero de la lista quieres cambiar (0,1,2)"))
                frut = input(print("que fruta quieres cambiar por la anterior "))
                if numero == 0:                  
                    frutas[0] = frut #cambiando el segundo elememnto osea banana 
                    print(frutas)
                    break
                elif numero == 1:
                    frutas[1] = frut #cambiando el segundo elememnto osea banana 
                    print(frutas)
                    break
                elif numero == 2:
                    frutas[2] = frut #cambiando el segundo elememnto osea banana 
                    print(frutas)
                    break
                else:
                    print("opcion no valida")
            elif opcion == 3:
                nueva = input(print("que fruta quieres agregar? "))
                frutas.append(nueva) #se añade naranja a la lista 
                print(frutas) 
            elif opcion == 4:
                #borra de elemnetos
                borrar = input(print("que numero de lista quieres borrar"))
                frutas.remove(borrar) #se elimina pera de lista 
                print(frutas)
            elif opcion == 5:
                #iterar a traves de una lista 
                for fruta in frutas:
                 print(fruta) #imprimiendo cada elemento de la lista    
            elif opcion == 5:
                break
            else:
                print("Opción no válida, por favor elige entre 1 y 5.")
        except ValueError:
            print("Por favor ingresa un número válido.")
