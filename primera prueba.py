def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convertidor_de_C_a_F():
    while True:
        celsius_input = input("Ingresa la temperatura en grados Celsius: ")
        try:
            celsius = float(celsius_input)
            if celsius < -273.15:
                print("El número ingresado es menor o igual al cero absoluto (-273.15°C). Por favor, intenta de nuevo.")
                continue
            if '.' in celsius_input:
                decimal_part = celsius_input.split('.')[1]
                if len(decimal_part) > 4:
                    print("El número tiene más de 4 decimales. Por favor, intenta de nuevo.")
                    continue
            fahrenheit = celsius_a_fahrenheit(celsius)
            # Eliminar ceros innecesarios
            celsius_str = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            fahrenheit_str = ('{:.4f}'.format(fahrenheit)).rstrip('0').rstrip('.')
            print(f"{celsius_str} grados Celsius son {fahrenheit_str} grados Fahrenheit.")
            break
        except ValueError:
            print("Valor no válido. Por favor, ingresa un número.")

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def convertidor_de_F_a_C():
    while True:
        fahrenheit_input = input("Ingresa la temperatura en grados Fahrenheit: ")
        try:
            fahrenheit = float(fahrenheit_input)
            if fahrenheit < -459.67 or fahrenheit == -459.67 :
                print("El número ingresado es menor o igual al cero absoluto (-459.67°F). Por favor, intenta de nuevo.")
                continue
            if '.' in fahrenheit_input:
                decimal_part = fahrenheit_input.split('.')[1]
                if len(decimal_part) > 4:
                    print("El número tiene más de 4 decimales. Por favor, intenta de nuevo.")
                    continue
            celsius = fahrenheit_a_celsius(fahrenheit)
            # Eliminar ceros innecesarios
            fahrenheit_str = ('{:.4f}'.format(fahrenheit)).rstrip('0').rstrip('.')
            celsius_str = ('{:.4f}'.format(celsius)).rstrip('0').rstrip('.')
            print(f"{fahrenheit_str} grados Fahrenheit son {celsius_str} grados Celsius.")
            break
        except ValueError:
            print("Valor no válido. Por favor, ingresa un número.")


while True:
    print("Convertidor")
    print("\n1. Fahrenheit a Celsius\n2. Celsius a Fahrenheit\n3. Salir")
    opcion = input("¿Qué opción quieres realizar? ")

    if opcion == "1":
        convertidor_de_F_a_C()
    elif opcion == "2":
        convertidor_de_C_a_F()
    elif opcion == "3":
        print("Saliendo del menú.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

