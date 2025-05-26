import tkinter as tk
import datetime
def saludar():
  print ("hola")
def tiempo():
  tiempo = datetime.datetime.now()
  print (tiempo)
ventana = tk.Tk()
ventana.title("Mi primera gilada")
ventana.geometry("600x400")
boton = tk.Button(ventana, text="pulsame", font=("Arial", 20), command=tiempo)
boton.pack()
ventana.mainloop()
