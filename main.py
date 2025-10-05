import tkinter as tk
from tkinter import messagebox

def calcular_calificacion():
    try:
        nota = float(entry_nota.get())

        if nota < 0 or nota > 20:
            messagebox.showerror("Error", "La nota debe estar entre 0 y 20.")
            return

        if 18 <= nota <= 20:
            calificacion = "AD"
        elif 14 <= nota < 17:
            calificacion = "A"
        elif 11 <= nota < 14:
            calificacion = "B"
        elif 0 <= nota < 11:
            calificacion = "C"

        label_resultado.config(text=f"Calificación: {calificacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una nota válida.")

ventana = tk.Tk()
ventana.title("Sistema de Calificaciones")

label_instrucciones = tk.Label(ventana, text="Ingresa la nota del estudiante (0-20):")
label_instrucciones.pack()

entry_nota = tk.Entry(ventana)
entry_nota.pack()

button_calcular = tk.Button(ventana, text="Calcular Calificación", command=calcular_calificacion)
button_calcular.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()
