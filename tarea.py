import random

def jugar_adivinanza():
    palabras = ["messi", "suarez", "neymar", "roben", "kroos", "modric", "cristiano", "ochoa", "chicharito", "pique"]
    palabra_secreta = random.choice(palabras)
    intentos = 3
    letras_adivinadas = []
    
    print("Bienvenido al juego de adivinanzas del mundial brazil 2014. Adivina la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    
    while intentos > 0:
        # Mostrar la palabra con las letras adivinadas
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
        
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        
        # Pedir al usuario una letra
        letra_usuario = input("Ingresa una letra: ").lower()
        
        if letra_usuario in letras_adivinadas:
            print("Ya has ingresado esta letra. Intenta con otra.")
        elif letra_usuario in palabra_secreta:
            print("¡Bien! Has adivinado una letra.")
            letras_adivinadas.append(letra_usuario)
        else:
            print("Incorrecto. Intenta de nuevo.")
            intentos -= 1
        
        # Verificar si se ha adivinado la palabra completa
        palabra_completa = True
        for letra in palabra_secreta:
            if letra not in letras_adivinadas:
                palabra_completa = False
                break
        
        if palabra_completa:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break
    
    if intentos == 0:
        print("Lo siento, te has quedado sin intentos. La palabra secreta era:", palabra_secreta)

jugar_adivinanza()