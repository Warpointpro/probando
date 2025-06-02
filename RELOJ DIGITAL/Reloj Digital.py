#primero importamos las librerias que vamos a utilizar
from tkinter import *
from tkinter.ttk import *
from time import strftime
#definimos el nombre a la ventana y le damos un tamaño
app = Tk()
app.title("Reloj Digital")
app.geometry("400x200")
#creamos un frame para la hora
frame_hora = Frame()
frame_hora.pack(pady=20)
#esto solo es para darle estilo a la ventana
etiqueta_hora = Label(frame_hora, font=("Arial", 60), background="white", foreground="black", text="H:M:S", anchor="center")
etiqueta_hora.pack(padx=20, pady=20)
#en esta parte solo defino la funcion la cual se encargara de actualizar la hora en 1000 milisegundos lo cual equivalen a 1 segundo
def actualizar_hora():
    hora_actual = strftime("%H:%M:%S")
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_hora)
actualizar_hora()
#por ultimo invocamos la aplicacion para mostrarse en la pantalla
app.mainloop()
