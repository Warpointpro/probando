from tkinter import *
from tkinter.ttk import *
from time import strftime
app = Tk()
app.title("Reloj Digital")
app.geometry("400x200")
frame_hora = Frame()
frame_hora.pack(pady=20)
etiqueta_hora = Label(frame_hora, font=("Arial", 60), background="white", foreground="black", text="H:M:S", anchor="center")
etiqueta_hora.pack(padx=20, pady=20)
def actualizar_hora():
    hora_actual = strftime("%H:%M:%S")
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_hora)
actualizar_hora()
app.mainloop()
