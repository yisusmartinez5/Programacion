#Temperatutras
#celsius

def convertir_celsius():
    while True:
        celsius_a = input("ingresa la temperatura en celsius ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
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
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#Fahrenheid

def convertir_fahrenheid():
    while True:
        fahrenheid_a = input("ingresa la temperatura en fahrenheid ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
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
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#Kelvin
#validacion y eliminar ceros
def convertir_kelvin():
    while True:
        kelvin_a = input("ingresa la temperatura en kelvin ( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
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
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")
