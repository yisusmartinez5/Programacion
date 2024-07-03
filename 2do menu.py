#presion

#toneladas
def convertir_tonelada():
    while True:
        tonelada_a = input("ingresa la cantidad en toneladas: ")
        try:
            if '.' in tonelada_a and tonelada_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            tonelada = float(tonelada_a)
            if tonelada < 0 or tonelada == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in tonelada_a :
                decimal = tonelada_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            gramo = tonelada * 1000
            kilogramo = tonelada * 35.274
            libra = tonelada * 2.205
            onza = tonelada /1000
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_ton = ('{:.4f}'.format(tonelada)).rstrip('0').rstrip('.')
            resultado_gra = ('{:.4f}'.format(gramo)).rstrip('0').rstrip('.')
            resultado_kil = ('{:.4f}'.format(kilogramo)).rstrip('0').rstrip('.')
            resultado_lib = ('{:.4f}'.format(libra)).rstrip('0').rstrip('.')
            resultado_onz = ('{:.4f}'.format(onza)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. gramos\n2. tonelada\n3. libra\n4. tonelada ")
             opcion = input("¿Los toneladas ingresados a que unidad la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_ton} toneladas son {resultado_gra} gramos")
                break
             elif opcion == "2":
                print(f"{resultado_ton} toneladas son {resultado_kil} kilogramos")
                break
             elif opcion == "3":
                print(f"{resultado_ton} toneladas son {resultado_lib} libras")
                break
             elif opcion == "4":
                 print(f"{resultado_ton} toneladas son {resultado_onz} toneladas")
                 break            
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en toneladas? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")