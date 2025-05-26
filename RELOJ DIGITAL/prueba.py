import tkinter as tk
from datetime import datetime

def actualizar_hora():
    # Obtener la hora actual en formato 24 horas: HH:MM:SS
    hora_actual = datetime.now().strftime("%H:%M:%S")
    lbl_hora.config(text=hora_actual)
    # Actualiza la hora cada 1000 ms (1 segundo)
    lbl_hora.after(1000, actualizar_hora)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("400x200")
ventana.config(bg="black")

# Cambia la fuente a una que tenga un estilo pixelado, por ejemplo "Digital-7 Mono".
# Asegúrate de tener instalada la fuente en tu sistema.
lbl_hora = tk.Label(ventana, text="", font=("Digital-7 Mono", 48), fg="lime", bg="black")
lbl_hora.pack(expand=True)

# Iniciar la actualización del reloj
actualizar_hora()

ventana.mainloop()