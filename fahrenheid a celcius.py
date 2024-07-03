#longitud
 
#centimetros          
def convertir_centimetro():
    while True:
        centimetros_a = input("ingresa la medida en centimetros: ")
        try:
            if '.' in centimetros_a and centimetros_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            centimetros = float(centimetros_a)
            if centimetros < 0 or centimetros == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in centimetros_a :
                decimal = centimetros_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la medida.")
                    continue
            metros = centimetros / 100
            milla = centimetros / 160900
            yarda = centimetros / 91.44
            pulgada = centimetros / 2.54
            pies = centimetros / 30.48
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_mil = ('{:.4f}'.format(milla)).rstrip('0').rstrip('.')
            resultado_yar = ('{:.4f}'.format(yarda)).rstrip('0').rstrip('.')
            resultado_pul = ('{:.4f}'.format(pulgada)).rstrip('0').rstrip('.')
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. Metros\n2. Milla\n3. Yarda\n4. Pulgada\n5. Pie ")
             opcion = input("¿Los centimetros ingresados a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_cen} centimetros son {resultado_met} metros")
                break
             elif opcion == "2":
                print(f"{resultado_cen} centimetros son {resultado_mil} millas")
                break
             elif opcion == "3":
                print(f"{resultado_cen} centimetros son {resultado_yar} yardas")
                break
             elif opcion == "4":
                 print(f"{resultado_cen} centimetros son {resultado_pul} pulgadas")
                 break
             elif opcion == "5":
                 print(f"{resultado_cen} centimetros son {resultado_pie} pies")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en centimetros? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")
                    
#metros
def convertir_metros():
    while True:
        metros_a = input("ingresa la medida en metros: ")
        try:
            if '.' in metros_a and metros_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")    
                continue
            metros = float(metros_a)
            if metros < 0 or metros == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in metros_a :
                decimal = metros_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            centimetros = metros * 100
            milla = metros / 1609
            yarda = metros * 1.094
            pulgada = metros * 39.37
            pies = metros * 3.281
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_mil = ('{:.4f}'.format(milla)).rstrip('0').rstrip('.')
            resultado_yar = ('{:.4f}'.format(yarda)).rstrip('0').rstrip('.')
            resultado_pul = ('{:.4f}'.format(pulgada)).rstrip('0').rstrip('.')
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. centimetros\n2. Milla\n3. Yarda\n4. Pulgada\n5. Pie ")
             opcion = input("¿Los metros ingresados a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_met} metros son {resultado_cen} centimetros")
                break
             elif opcion == "2":
                print(f"{resultado_met} metros son {resultado_mil} millas")
                break
             elif opcion == "3":
                print(f"{resultado_met} metros son {resultado_yar} yardas")
                break
             elif opcion == "4":
                 print(f"{resultado_met} metros son {resultado_pul} pulgadas")
                 break
             elif opcion == "5":
                 print(f"{resultado_met} metros son {resultado_pie} pies")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad metros? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")

#millas
def convertir_milla():
    while True:
        millas_a = input("ingresa la medida en millas: ")
        try:
            if '.' in millas_a and millas_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            millas = float(millas_a)
            if millas < 0 or millas == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in millas_a :
                decimal = millas_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            centimetros = millas * 160900
            metros = millas * 1609.34
            yarda = millas * 1760
            pulgada = millas * 63360
            pies = millas * 5280
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_mil = ('{:.4f}'.format(millas)).rstrip('0').rstrip('.')
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_yar = ('{:.4f}'.format(yarda)).rstrip('0').rstrip('.')
            resultado_pul = ('{:.4f}'.format(pulgada)).rstrip('0').rstrip('.')
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. centimetros\n2. Metros\n3. Yarda\n4. Pulgada\n5. Pie ")
             opcion = input("¿Las millas ingresadas a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_mil} millas son {resultado_cen} centimetros")
                break
             elif opcion == "2":
                print(f"{resultado_mil} millas son {resultado_met} metros")
                break
             elif opcion == "3":
                print(f"{resultado_mil} millas son {resultado_yar} yardas")
                break
             elif opcion == "4":
                 print(f"{resultado_mil} millas son {resultado_pul} pulgadas")
                 break
             elif opcion == "5":
                 print(f"{resultado_mil} millas son {resultado_pie} pies")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en millas? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")
            
#yardas            
def convertir_yarda():
    while True:
        yarda_a = input("ingresa la medida en yardas: ")
        try:
            if '.' in yarda_a and yarda_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            yardas = float(yarda_a)
            if yardas < 0 or yardas == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in yarda_a :
                decimal = yarda_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            centimetros = yardas * 91.44
            metros = yardas / 1.094
            milla = yardas / 1760
            pulgada = yardas * 36
            pies = yardas * 3
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_yar = ('{:.4f}'.format(yardas)).rstrip('0').rstrip('.')
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_mil = ('{:.4f}'.format(milla)).rstrip('0').rstrip('.')
            resultado_pul = ('{:.4f}'.format(pulgada)).rstrip('0').rstrip('.')
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. centimetros\n2. Metros\n3. millas\n4. Pulgada\n5. Pie ")
             opcion = input("¿Las yardas ingresadas a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_yar} yardas son {resultado_cen} centimetros")
                break
             elif opcion == "2":
                print(f"{resultado_yar} yardas son {resultado_met} metros")
                break
             elif opcion == "3":
                print(f"{resultado_yar} yardas son {resultado_mil} millas")
                break
             elif opcion == "4":
                 print(f"{resultado_yar} yardas son {resultado_pul} pulgadas")
                 break
             elif opcion == "5":
                 print(f"{resultado_yar} yardas son {resultado_pie} pies")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en yardas? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")
            
#Pulgadas
def convertir_pulgada():
    while True:
        pulgada_a = input("ingresa la medida en pulgadas: ")
        try:
            if '.' in pulgada_a and pulgada_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            pulgadas = float(pulgada_a)
            if pulgadas < 0 or pulgadas == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in pulgada_a :
                decimal = pulgada_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            centimetros = pulgadas * 2.54
            metros = pulgadas / 39.37
            milla = pulgadas / 63360
            yarda = pulgadas / 36
            pies = pulgadas / 12
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_pul = ('{:.4f}'.format(pulgadas)).rstrip('0').rstrip('.')
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_mil = ('{:.4f}'.format(milla)).rstrip('0').rstrip('.')
            resultado_yar = ('{:.4f}'.format(yarda)).rstrip('0').rstrip('.')
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. centimetros\n2. Metros\n3. millas\n4. yardas\n5. Pie ")
             opcion = input("¿Las yardas ingresadas a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_pul} pulgadas son {resultado_cen} centimetros")
                break
             elif opcion == "2":
                print(f"{resultado_pul} pulgadas son {resultado_met} metros")
                break
             elif opcion == "3":
                print(f"{resultado_pul} pulgadas son {resultado_mil} millas")
                break
             elif opcion == "4":
                 print(f"{resultado_pul} pulgadas son {resultado_yar} yardas")
                 break
             elif opcion == "5":
                 print(f"{resultado_pul} pulgadas son {resultado_pie} pies")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en yardas? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")

#pies
def convertir_pies():
    while True:
        pies_a = input("ingresa la medida en pies: ")
        try:
            if '.' in pies_a and pies_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            pies = float(pies_a)
            if pies < 0 or pies == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in pies_a :
                decimal = pies_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            centimetros = pies * 30.48
            metros = pies / 3.281
            milla = pies / 5280
            yarda = pies / 3
            pulgadas = pies * 12
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_pie = ('{:.4f}'.format(pies)).rstrip('0').rstrip('.')
            resultado_cen = ('{:.4f}'.format(centimetros)).rstrip('0').rstrip('.')
            resultado_met = ('{:.4f}'.format(metros)).rstrip('0').rstrip('.')
            resultado_mil = ('{:.4f}'.format(milla)).rstrip('0').rstrip('.')
            resultado_yar = ('{:.4f}'.format(yarda)).rstrip('0').rstrip('.')
            resultado_pul = ('{:.4f}'.format(pulgadas)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. centimetros\n2. Metros\n3. millas\n4. yardas\n5. Pulgadas ")
             opcion = input("¿Las yardas ingresadas a que medida la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_pie} pies son {resultado_cen} centimetros")
                break
             elif opcion == "2":
                print(f"{resultado_pie} pies son {resultado_met} metros")
                break
             elif opcion == "3":
                print(f"{resultado_pie} pies son {resultado_mil} millas")
                break
             elif opcion == "4":
                 print(f"{resultado_pie} pies son {resultado_yar} yardas")
                 break
             elif opcion == "5":
                 print(f"{resultado_pie} pies son {resultado_pul} pulgadas")
                 break             
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en pies? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no válid0. ingresa un número correcto .")


#Masa

#gramos
def convertir_gramo():
    while True:
        gramo_a = input("ingresa la cantidad en gramos: ")
        try:
            if '.' in gramo_a and gramo_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            gramo = float(gramo_a)
            if gramo < 0 or gramo == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in gramo_a :
                decimal = gramo_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            kilogramo = gramo / 1000
            onza = gramo  / 28.35
            libra = gramo / 453.6
            tonelada = gramo /1_000_000
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_gra = ('{:.4f}'.format(gramo)).rstrip('0').rstrip('.')
            resultado_kil = ('{:.4f}'.format(kilogramo)).rstrip('0').rstrip('.')
            resultado_onz = ('{:.4f}'.format(onza)).rstrip('0').rstrip('.')
            resultado_lib = ('{:.4f}'.format(libra)).rstrip('0').rstrip('.')
            resultado_ton = ('{:.4f}'.format(tonelada)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. kilogramos\n2. onza\n3. libra\n4. tonelada ")
             opcion = input("¿Los gramos ingresados a que unidad la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_gra} gramos son {resultado_kil} kilogramos")
                break
             elif opcion == "2":
                print(f"{resultado_gra} gramos son {resultado_onz} onzas")
                break
             elif opcion == "3":
                print(f"{resultado_gra} gramos son {resultado_lib} libras")
                break
             elif opcion == "4":
                 print(f"{resultado_gra} gramos son {resultado_ton} toneladas")
                 break            
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en gramos? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")

#kilogramo
def convertir_kilogramo():
    while True:
        kilogramo_a = input("ingresa la cantidad en kilogramos: ")
        try:
            if '.' in kilogramo_a and kilogramo_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            kilogramo = float(kilogramo_a)
            if kilogramo < 0 or kilogramo == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in kilogramo_a :
                decimal = kilogramo_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            gramo = kilogramo * 1000
            onza = kilogramo * 35.274
            libra = kilogramo * 2.205
            tonelada = kilogramo /1000
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_kil = ('{:.4f}'.format(kilogramo)).rstrip('0').rstrip('.')
            resultado_gra = ('{:.4f}'.format(gramo)).rstrip('0').rstrip('.')
            resultado_onz = ('{:.4f}'.format(onza)).rstrip('0').rstrip('.')
            resultado_lib = ('{:.4f}'.format(libra)).rstrip('0').rstrip('.')
            resultado_ton = ('{:.4f}'.format(tonelada)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. gramos\n2. onza\n3. libra\n4. tonelada ")
             opcion = input("¿Los kilogramos ingresados a que unidad la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_kil} kilos son {resultado_gra} gramos")
                break
             elif opcion == "2":
                print(f"{resultado_kil} kilos son {resultado_onz} onzas")
                break
             elif opcion == "3":
                print(f"{resultado_kil} kilos son {resultado_lib} libras")
                break
             elif opcion == "4":
                 print(f"{resultado_kil} kilos son {resultado_ton} toneladas")
                 break            
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en kilos? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")

#onza
def convertir_onza():
    while True:
        onza_a = input("ingresa la cantidad en onzas: ")
        try:
            if '.' in onza_a and onza_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            onza = float(onza_a)
            if onza < 0 or onza == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in onza_a :
                decimal = onza_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            gramo = onza * 28.35
            kilogramo = onza / 35.274
            libra = onza / 16
            tonelada = onza / 35270    
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_onz = ('{:.4f}'.format(onza)).rstrip('0').rstrip('.')
            resultado_gra = ('{:.4f}'.format(gramo)).rstrip('0').rstrip('.')
            resultado_kil = ('{:.4f}'.format(kilogramo)).rstrip('0').rstrip('.')
            resultado_lib = ('{:.4f}'.format(libra)).rstrip('0').rstrip('.')
            resultado_ton = ('{:.4f}'.format(tonelada)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. gramos\n2. kilogramos\n3. libra\n4. tonelada ")
             opcion = input("¿Los onzas ingresados a que unidad la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_onz} onzas son {resultado_gra} gramos")
                break
             elif opcion == "2":
                print(f"{resultado_onz} onzas son {resultado_kil} kilogramos")
                break
             elif opcion == "3":
                print(f"{resultado_onz} onzas son {resultado_lib} libras")
                break
             elif opcion == "4":
                 print(f"{resultado_onz} onzas son {resultado_ton} toneladas")
                 break            
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en onzas? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")

#libras
def convertir_libra():
    while True:
        libra_a = input("ingresa la cantidad en libras: ")
        try:
            if '.' in libra_a and libra_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            libra = float(libra_a)
            if libra < 0 or libra == 0 :
                print("El dato que has ingresado esta mal. Ingresa de nuevo el dato. ")
                continue
            if '.' in libra_a :
                decimal = libra_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo el dato.")
                    continue
            gramo = libra * 453.6
            kilogramo = libra /  2.205
            tonelada = libra / 2205
            onza = libra *16
            
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_lib = ('{:.4f}'.format(libra)).rstrip('0').rstrip('.')
            resultado_gra = ('{:.4f}'.format(gramo)).rstrip('0').rstrip('.')
            resultado_kil = ('{:.4f}'.format(kilogramo)).rstrip('0').rstrip('.')
            resultado_ton = ('{:.4f}'.format(tonelada)).rstrip('0').rstrip('.')
            resultado_onz = ('{:.4f}'.format(onza)).rstrip('0').rstrip('.')
           
            while True:
             print("\n1. gramos\n2. kilogramos\n3. onzas\n4. toneladas ")
             opcion = input("¿Los libras ingresados a que unidad la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_lib} libras son {resultado_gra} gramos")
                break
             elif opcion == "2":
                print(f"{resultado_lib} libras son {resultado_kil} kilogramos")
                break
             elif opcion == "3":
                print(f"{resultado_lib} libras son {resultado_onz} onzas")
                break
             elif opcion == "4":
                 print(f"{resultado_lib} libras son {resultado_ton} toneladas")
                 break            
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en libras? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("dato no valido. ingresa un número correcto .")


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
                    print("El número tiene más de 4 decimales. Ingresa de nuevo el dato.")
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
             print("\n1. gramos\n2. tonelada\n3. libra\n4. onzas ")
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
                 print(f"{resultado_ton} toneladas son {resultado_onz} onzas")
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




#temperaturas
#celsius

def convertir_celsius():
    while True:
        celsius_a = input("ingresa la temperatura en celsius ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
            if '.' in celsius_a and celsius_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            celsius = float(celsius_a)
            if celsius < -273.15 or celsius == -273.15 :
                print("La temperatura que has ingresado es menor o igual al cero absoluto (-273.15°C). Ingresa de nuevo la temperatura. ")
                continue
            if '.' in celsius_a :
                decimal = celsius_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
#formula para la conversion Celsius
            fahrenheid = celsius * 9/5 +32
            kelvin = celsius + 273.15
#eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            while True:
             print("\n1.Fahrenheid \n2. kelvin ")
             opcion = input("¿Los datos ingresados a que temperatura la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_cel} celsius son {resultado_fah} fahrenheid")
                break
             elif opcion == "2":
                print(f"{resultado_cel} celsius son {resultado_kel} kelvin")
                break   
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en celsius? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#Fahrenheid

def convertir_fahrenheid():
    while True:
        fahrenheid_a = input("ingresa la temperatura en fahrenheid ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
            if '.' in fahrenheid_a and fahrenheid_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            fahrenheid = float(fahrenheid_a)
            if fahrenheid < -459.67 or fahrenheid == -459.67 :
                print("La temperatura que has ingresado es menor o igual al cero absoluto (-459.67°F). Ingresa de nuevo la temperatura. ")
                continue
            if '.' in fahrenheid_a :
                decimal = fahrenheid_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
#Formulas para las conversiones
            celsius = (fahrenheid - 32) * 5.0 / 9.0
            kelvin = (fahrenheid - 32) / 1.8 + 273.15
#eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            while True:
             print("\n1.celsius \n2. kelvin ")
             opcion = input("¿Los datos ingresados a que temperatura la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_fah} Fahrenheid son {resultado_cel} celsius")
                break
             elif opcion == "2":
                print(f"{resultado_fah} Fahrenheid son {resultado_kel} kelvin")
                break   
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en fahrenheid? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#Kelvin
#validacion y eliminar ceros
def convertir_kelvin():
    while True:
        kelvin_a = input("ingresa la temperatura en kelvin ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
            if '.' in kelvin_a and kelvin_a.endswith('.'):
                print("El dato que has ingresado no tiene decimales. Ingresa de nuevo el dato.")
                continue
            kelvin = float(kelvin_a)
            if kelvin < 0 or kelvin == 0 :
                print("La temperatura que has ingresado es menor o igual al cero absoluto. Ingresa de nuevo la temperatura. ")
                continue
            if '.' in kelvin_a :
                decimal = kelvin_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
#formulas para las conversiones
            celsius = kelvin - 273.15
            fahrenheid = (kelvin - 273.15) * 9/5 + 32
#eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            while True:
             print("\n1.celsius \n2. Fahrenheid")
             opcion = input("¿Los datos ingresados a que temperatura la quieres convertir? ")

             if opcion == "1":
                print(f"{resultado_kel} kelvin son {resultado_cel} celsius")
                break
             elif opcion == "2":
                print(f"{resultado_kel} kelvin son {resultado_fah} fahrenheid")
                break   
             else:
                print("Opción no válida. Por favor, elige una opción. ")
            while True:
             otra_conversion = input("¿Quieres convertir a otra unidad en kelvin? (si/no): ").strip().lower()
             if otra_conversion in ['si', 'sí']:
                break
             elif otra_conversion == 'no':
                return
             else:
                print("Dato no válido. Ingresa 'si' o 'no'.")
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")



while True:
    print("Convertidor")
    print("\n1. longitud\n2. Masa\n3. Presion\n4. Temperatura\n5. Tiempo\n6. Velocidad\n7.columen\n8. area\n9. Salir ")
    opcion = input("¿Qué unidad quieres convertir? ")

    if opcion == "1":
        while True:
             print("\n1. Centimetros \n2.Metros\n3. Milla\n4. Yarda\n5. Pulgada\n6. Pie\n7. Salir ")
             opcion = input("¿Que unidad de medida quieres convertir? o presiona 7 si quieres salir ")

             if opcion == "1":
                 convertir_centimetro()
             elif opcion == "2":
                 convertir_metros()
             elif opcion == "3":
                 convertir_milla()
             elif opcion == "4":
                 convertir_yarda()
             elif opcion == "5":
                 convertir_pulgada() 
             elif opcion == "6" :
                 convertir_pies() 
             elif opcion == "7" :
                 break         
             else:
                 print("Opción no válida. Por favor, elige una opción. ")      
    elif opcion == "2":
         while True:
             print("\n1. gramos \n2. kilogramos\n3. onza\n4. libra\n5. tonelada\n6. Salir ")
             opcion = input("¿Que unidad de medida quieres convertir? o presiona 6 si quieres salir ")

             if opcion == "1":
                 convertir_gramo()
             elif opcion == "2":
                 convertir_kilogramo()
             elif opcion == "3":
                 convertir_onza()
             elif opcion == "4":
                 convertir_libra()
             elif opcion == "5":
                 convertir_tonelada()
             elif opcion == "6" :
                 break         
             else:
                 print("Opción no válida. Por favor, elige una opción. ")
    elif opcion == "3":
         while True:
             print("\n1. atmosferas \n2. BAR\n3. libra por pulgada cuadrada\n4. Pascal\n5. Torr\n6. Salir ")
             opcion = input("¿Que unidad de medida quieres convertir? o presiona 6 si quieres salir ")

             if opcion == "1":
                 convertir_gramo()
             elif opcion == "2":
                 convertir_kilogramo()
             elif opcion == "3":
                 convertir_onza()
             elif opcion == "4":
                 convertir_yarda()
             elif opcion == "5":
                 convertir_pulgada() 
             elif opcion == "6" :
                 convertir_tonelada() 
             elif opcion == "7" :
                 break         
             else:
                 print("Opción no válida. Por favor, elige una opción. ")
    elif opcion == "4":
         while True:
             print("\n1. Celsius \n2. Fhrenheid\n3. Kelvin\n4. Salir ")
             opcion = input("¿Que unidad de medida quieres convertir? o presiona 4 si quieres salir ")

             if opcion == "1":
                 convertir_celsius()
             elif opcion == "2":
                 convertir_fahrenheid()
             elif opcion == "3":
                 convertir_kelvin()  
             elif opcion == "4" :
                 break         
             else:
                 print("Opción no válida. Por favor, elige una opción. ")
    elif opcion == "5":
         convertir_centimetro()
    elif opcion == "6":
         convertir_centimetro()
    elif opcion == "7":
         convertir_centimetro()
    elif opcion == "8":
         convertir_centimetro()   
    elif opcion == "9":
        print("Saliendo del convertidor.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")