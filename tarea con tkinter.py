import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivinanza:
    def __init__(self, master):
        self.master = master
        self.palabras = ["messi", "suarez", "neymar", "roben", "kroos", "modric", "cristiano", "ochoa", "chicharito", "pique"]
        self.palabra_secreta = random.choice(self.palabras)
        self.intentos = 3
        self.letras_adivinadas = []

        self.master.title("Juego de Adivinanza")
        self.etiqueta_palabra = tk.Label(master, text="")
        self.etiqueta_intentos = tk.Label(master, text="")
        self.etiqueta_palabra.grid(row=0, column=0)
        self.etiqueta_intentos.grid(row=1, column=0)

        self.palabra_mostrada = "_" * len(self.palabra_secreta)
        self.actualizar_interfaz()

        self.entrada_letra = tk.Entry(master)
        self.entrada_letra.grid(row=2, column=0)
        self.boton_adivinar = tk.Button(master, text="Adivinar", command=self.adivinar_letra)
        self.boton_adivinar.grid(row=2, column=1)

    def actualizar_interfaz(self):
        self.etiqueta_palabra.config(text="Palabra: " + " ".join(self.palabra_mostrada))
        self.etiqueta_intentos.config(text="Intentos restantes: " + str(self.intentos))

    def adivinar_letra(self):
        letra_usuario = self.entrada_letra.get().lower()

        if letra_usuario in self.letras_adivinadas:
            messagebox.showinfo("Aviso", "Ya has ingresado esta letra. Intenta con otra.")
        elif letra_usuario in self.palabra_secreta:
            self.letras_adivinadas.append(letra_usuario)
            self.actualizar_palabra_mostrada()
            if "_" not in self.palabra_mostrada:
                messagebox.showinfo("Felicidades", f"¡Has adivinado la palabra secreta: {self.palabra_secreta}!")
                self.master.destroy()
        else:
            self.intentos -= 1
            self.actualizar_interfaz()
            if self.intentos == 0:
                messagebox.showinfo("Fin del Juego", f"Lo siento, te has quedado sin intentos. La palabra secreta era: {self.palabra_secreta}")
                self.master.destroy()

    def actualizar_palabra_mostrada(self):
        self.palabra_mostrada = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                self.palabra_mostrada += letra
            else:
                self.palabra_mostrada += "_"
        self.actualizar_interfaz()

def main():
    root = tk.Tk()
    juego = JuegoAdivinanza(root)
    root.mainloop()

if __name__ == "__main__":
    main()