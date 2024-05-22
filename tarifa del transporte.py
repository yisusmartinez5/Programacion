edad = int(input("ingresa tu edad por favor: "))
hora = int(input("ingresa la hora en un formato de 24 hrs: "))
boleto = 300
if edad < 5: print("puedes viajar gratis")
elif edad >= 65: 
    descuento = boleto * .30
    total = boleto - descuento
    print(f"tuvo un descuento de %30 y se le desconto", descuento, "pesos ")
    print(f"y su total a pagar es de: ", total, "pesos" )
else:
    if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
        total = boleto + 50
        print(f"se le aplico un cargo de 50 pesos por la hora pico asi que su boleto costo " , total,)
    else:
        print(f"el costo de su boleto fue de ", boleto,)