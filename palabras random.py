import random
import string

def generar_palabra_aleatoria():
    letras = string.ascii_lowercase
    palabra = random.choice(letras) + random.choice(letras) + random.choice(letras)
    return palabra

def comparar_palabras(palabra, adivinanza):
    correctas = 0
    for i in range(3):
        if palabra[i] == adivinanza[i]:
            correctas += 1
    return correctas

def jugar():
    palabra_secreta = generar_palabra_aleatoria()
    intentos = 20
    
    print("adivina la palabra.")
    print("Debes adivinar una palabra de tres letras.")
    print("Tienes", intentos, "intentos.")

    while intentos > 0:
        adivinanza = input("Introduce tu adivinanza: ").lower()
        
        if len(adivinanza) != 3 or not adivinanza.isalpha():
            print("Por favor, introduce una palabra válida de tres letras.")
            continue
        
        correctas = comparar_palabras(palabra_secreta, adivinanza)
        
        if correctas == 3:
            print(" Adivinaste la palabra:", palabra_secreta)
            break
        else:
            intentos -= 1
            print("Tienes", correctas, "letra(s) correcta(s) en la posición correcta.")
            print("Te quedan", intentos, "intento(s).")

    if intentos == 0:
        print("Lo siento, te quedaste sin intentos. La palabra era:", palabra_secreta)

# Iniciar el juego
jugar()