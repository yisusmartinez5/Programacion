import random
import tkinter as tk
from tkinter import messagebox

def jugar_adivinanza():
    def verificar_letra():
        letra_usuario = letra_entry.get().lower()
        letra_entry.delete(0, tk.END)
        
        if letra_usuario in letras_adivinadas:
            messagebox.showinfo("Letra repetida", "Ya has ingresado esta letra. Intenta con otra.")
        elif letra_usuario in palabra_secreta:
            letras_adivinadas.append(letra_usuario)
            actualizar_palabra_mostrada()
            if palabra_mostrada == palabra_secreta:
                messagebox.showinfo("¡Felicidades!", f"¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                ventana.destroy()
        else:
            intentos.set(intentos.get() - 1)
            if intentos.get() == 0:
                messagebox.showinfo("Fin del juego", f"Lo siento, te has quedado sin intentos. La palabra secreta era: {palabra_secreta}")
                ventana.destroy()

    def actualizar_palabra_mostrada():
        palabra_mostrada = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
        palabra_label.config(text=palabra_mostrada)

    ventana = tk.Tk()
    ventana.title("Adivinanza del Mundial Brazil 2014")

    palabra_secreta = random.choice(["messi", "suarez", "neymar", "roben", "kroos", "modric", "cristiano", "ochoa", "chicharito", "pique"])
    letras_adivinadas = []
    intentos = tk.IntVar(value=3)

    palabra_label = tk.Label(ventana, text="", font=("Arial", 24))
    palabra_label.pack(pady=10)

    letra_entry = tk.Entry(ventana, font=("Arial", 14))
    letra_entry.pack(pady=5)

    verificar_button = tk.Button(ventana, text="Verificar letra", command=verificar_letra)
    verificar_button.pack(pady=5)

    intentos_label = tk.Label(ventana, textvariable=intentos, font=("Arial", 16))
    intentos_label.pack(pady=5)

    actualizar_palabra_mostrada()

    ventana.mainloop()

jugar_adivinanza()