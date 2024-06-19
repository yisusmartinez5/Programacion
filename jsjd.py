menu_comidas = {
    "Hamburguesa": 100,
    "Pizza": 120,
    "Tacos": 80,
    "Sushi": 150,
    "Ensalada": 90,
    "Pasta": 110,
    "Sándwich": 95,
    "Pollo frito": 130,
    "Hot dog": 85,
    "Filete": 140
}

menu_bebidas = {
    "Agua": 20,
    "Refresco": 30,
    "Jugo": 25,
    "Café": 35,
    "Té": 25,
    "Cerveza": 40,
    "Vino": 50,
    "Licuado": 45,
    "Margarita": 60,
    "Cóctel": 55
}

# Función para mostrar el menú
def mostrar_menu(menu):
    print("Menú:")
    for item, precio in menu.items():
        print(f"{item}: ${precio}")

# Función para calcular el total del pedido
def calcular_total(pedido, menu):
    total = 0
    for item in pedido:
        if item in menu:
            total += menu[item]
    return total

# Mostrar los menús de comidas y bebidas
print("Bienvenido al restaurante:")
print("Comidas disponibles:")
mostrar_menu(menu_comidas)
print("\nBebidas disponibles:")
mostrar_menu(menu_bebidas)

# Hacer el pedido
pedido_comidas = []
pedido_bebidas = []

while True:
    opcion_comida = input("\nIngrese el nombre de la comida que desea pedir (o 'fin' para terminar): ")
    if opcion_comida.lower() == 'fin':
        break
    if opcion_comida in menu_comidas:
        pedido_comidas.append(opcion_comida)
    else:
        print("Lo siento, ese ítem no está en el menú de comidas.")

while True:
    opcion_bebida = input("\nIngrese el nombre de la bebida que desea pedir (o 'fin' para terminar): ")
    if opcion_bebida.lower() == 'fin':
        break
    if opcion_bebida in menu_bebidas:
        pedido_bebidas.append(opcion_bebida)
    else:
        print("Lo siento, ese ítem no está en el menú de bebidas.")

# Calcular el total del pedido
total_comidas = calcular_total(pedido_comidas, menu_comidas)
total_bebidas = calcular_total(pedido_bebidas, menu_bebidas)
total_pedido = total_comidas + total_bebidas

# Mostrar el total del pedido
print("\nResumen del pedido:")
print("Comidas pedidas:")
for comida in pedido_comidas:
    print(comida)
print("Total comidas: $", total_comidas)

print("\nBebidas pedidas:")
for bebida in pedido_bebidas:
    print(bebida)
print("Total bebidas: $", total_bebidas)

print("\nTotal del pedido: $", total_pedido)