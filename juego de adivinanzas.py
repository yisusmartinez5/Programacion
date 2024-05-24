#llamado a una libreria 
import random
#establecer un numero secreto
numero_secreto = random.rand(1000, 9999)
#el usuario adivinara el numero hasta que acierte
while True:
    intento = int(input("adivina el numero entre 1000 y 9999: "))
    if intento == numero_secreto:
        print("acertaste, tienes 8 en el parcial")
        break
    else:
        print("has fallado, vuelve a intentarlo")