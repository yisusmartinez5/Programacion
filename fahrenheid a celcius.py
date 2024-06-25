#formula para la conversion Celsius
def celsius_a_fahrenheid(celsius):
    return celsius * 9/5 +32
#validaciones y eliminar ceros
def convertir_celsius_fahrenheid():
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
            fahrenheid = celsius_a_fahrenheid(celsius)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            print(f"{resultado_cel} grados celsius son {resultado_fah} grados fahrenheid.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#formula para la conversion 2 Fahrenheid
def fahrenheid_a_celsius(fahrenheid):
    return (fahrenheid - 32) * 5.0 / 9.0
#validacion y eliminar ceros
def convertir_fahrenheid_celsius():
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
            celsius = fahrenheid_a_celsius(fahrenheid)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            print(f"{resultado_fah} grados fahrenheid son {resultado_cel} grados celsius.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")   
        

#formula para la conversion 3 Kelvin
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15
#validacion y eliminar ceros
def convertir_kelvin_a_celsius():
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
            celsius = kelvin_a_celsius(kelvin)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            print(f"{resultado_kel} kelvin son {resultado_cel} grados celcius.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")
            

#formula para la conversion 4 celcius a kelvin
def celsius_a_kelvin(celsius):
    return celsius + 273.15
#validacion y eliminar ceros
def convertir_celsius_a_kelvin():
    while True:
        celsius_a = input("ingresa la temperatura en grados celsius( recuerda que no debe ser menor ni igual a cero absoluto): ")
        try:
            celsius = float(celsius_a)
            if celsius < -273.15 or celsius == -273.15 :
                print("La temperatura que has ingresado es menor o igual al cero absoluto. Ingresa de nuevo la temperatura. ")
                continue
            if '.' in celsius_a :
                decimal = celsius_a.split('.')[1]
                if len(decimal) > 4:
                    print("El número tiene más de 4 decimales. Ingresa de nuevo la temperatura.")
                    continue
            kelvin = celsius_a_kelvin(celsius)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_cel = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            print(f"{resultado_cel} grados celsius son {resultado_kel} kelvin.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#formula para la conversion 5 Fahrenheid a Kelvin
def fahrenheid_a_Kelvin(fahrenheid):
    return (fahrenheid - 32) / 1.8 + 273.15
#validacion y eliminar ceros
def convertir_fahrenheid_kelvin():
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
            kelvin = fahrenheid_a_celsius(fahrenheid)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            print(f"{resultado_fah} grados fahrenheid son {resultado_kel} grados celsius.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


#formula para la conversion 6 Kelvin a fahrenheid
def kelvin_a_fahrenheid(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
#validacion y eliminar ceros
def convertir_kelvin_a_Fahrenheit():
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
            fahrenheid = kelvin_a_fahrenheid(kelvin)
            #eliminar ceros que no nos sirvan al momento de imprimir 
            resultado_kel = ('{:.4f}'.format(kelvin)).rstrip('0').rstrip('.')
            resultado_fah = ('{:.4f}'.format(fahrenheid)).rstrip('0').rstrip('.')
            print(f"{resultado_kel} kelvin son {resultado_fah} grados celcius.")
            break
        except ValueError:
            print("temperatura no válida. ingresa un número correcto .")


while True:
    print("Convertidor")
    print("\n1. Celsius a Fahrenheid\n2. Fahrenheit a Celsius\n3. Kelvin a Celsius\n4. Celsius a Kelvin\n5. fahrenheid a kelvin\n6. kelvin a fahrenheid\n7. Salir ")
    opcion = input("¿Qué opción quieres realizar? ")

    if opcion == "1":
        convertir_celsius_fahrenheid()
    elif opcion == "2":
        convertir_fahrenheid_celsius()
    elif opcion == "3":
        convertir_kelvin_a_celsius()
    elif opcion == "4":
        convertir_celsius_a_kelvin()
    elif opcion == "5":
        convertir_fahrenheid_kelvin()
    elif opcion == "6":
        convertir_kelvin_a_Fahrenheit()
    elif opcion == "7":
        print("Saliendo del convertidor.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
                