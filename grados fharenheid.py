def celsius_a_fahrenheit(celsius):
    """Convierte celsius a fahrenheit"""
    return round((celsius * 9/5) + 32, 4)

# ingresar la temperatura en Celsius con un límite de 4 decimales
temperatura_c_str = input("Ingresa la temperatura en Celsius porfavor no mas de 4 decimales: ")
try:
    temperatura_c = float("{:.4f}".format(float(temperatura_c_str)))
except ValueError:
    print("Error: Ingresa un número válido.")
    exit()

# Convertir temperatura a Fahrenheit
temperatura_f = celsius_a_fahrenheit(temperatura_c)

# Formatear el número a 4 decimales para imprimir
temperatura_f_formateada = "{:.4f}".format(temperatura_f)

# Imprimir la temperatura en Fahrenheit
print(f"La temperatura es {temperatura_f_formateada} grados Fahrenheit")

temperatura_f=float(input("ingresa la temperatura: "))
def celsius_a_fahrenheit(celsius):
    """convierte celsius a fahrenheit"""
    return (celsius* 9/5)+32
temperatura_f=celsius_a_fahrenheit (30)
print(f"la temperatura es {temperatura_f} grados fahrenheit")