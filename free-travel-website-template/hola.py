import tkinter as tk
from tkinter import messagebox
import time

def mostrar_mensaje():
    # Creamos una ventana nueva para la sorpresa
    ventana_sorpresa = tk.Toplevel()
    ventana_sorpresa.title("❤️ ¡Sorpresa! ❤️")
    ventana_sorpresa.geometry("400x300")
    ventana_sorpresa.configure(bg="#ff7eb9") # Color rosa vibrante

    # Decoración de corazones con texto
    label_corazon = tk.Label(
        ventana_sorpresa, 
        text="  ♥   ♥  \n♥       ♥\n ♥     ♥ \n  ♥   ♥  \n    ♥    ", 
        font=("Courier", 20, "bold"),
        bg="#ff7eb9",
        fg="white"
    )
    label_corazon.pack(pady=20)

    label_texto = tk.Label(
        ventana_sorpresa, 
        text="¡TE AMO!", 
        font=("Helvetica", 30, "bold italic"),
        bg="#ff7eb9",
        fg="white"
    )
    label_texto.pack()

def abrir_caja():
    # Efecto visual en el botón antes de abrir
    btn_caja.config(text="✨ ABRIENDO... ✨", state="disabled")
    root.update()
    time.sleep(1)
    mostrar_mensaje()
    btn_caja.config(text="📦 CAJA ABIERTA", state="normal")

# Ventana Principal
root = tk.Tk()
root.title("Caja Sorpresa")
root.geometry("350x450")
root.configure(bg="#4a148c") # Fondo morado profundo como el de la imagen

# Título
titulo = tk.Label(
    root, 
    text="Tienes un regalo especial", 
    font=("Arial", 14, "bold"),
    bg="#4a148c",
    fg="#e1bee7"
)
titulo.pack(pady=30)

# El botón que parece una caja
btn_caja = tk.Button(
    root, 
    text="📦\nPRESIONA AQUÍ", 
    font=("Arial", 18, "bold"),
    bg="#ffd700", # Color Dorado
    fg="#4a148c",
    padx=20,
    pady=20,
    relief="raised",
    borderwidth=5,
    command=abrir_caja
)
btn_caja.pack(pady=20)

# Decoración inferior
footer = tk.Label(
    root, 
    text="✨ Creado con amor ✨", 
    font=("Arial", 10, "italic"),
    bg="#4a148c",
    fg="#ba68c8"
)
footer.pack(side="bottom", pady=20)

root.mainloop()