import tkinter as tk
import time
import calendar
from datetime import datetime
import platform 
from zoneinfo import ZoneInfo
from temporizador import Temporizador
# Solo importar winsound si estamos en Windows
if platform.system() == "Windows":
    import winsound
# Variable global para formato de hora
formato_24h = False

# Inicializar última hora para controlar el sonido
ultima_hora_en_punto = -1

def reproducir_sonido():
    if platform.system() == "Windows":
        winsound.Beep(1000, 500)  # frecuencia, duración
    else:
        print("🔔 Sonido de hora en punto (no disponible en este sistema)")

def actualizar_reloj():
    global ultima_hora_en_punto

    ahora = datetime.now()
    hora_str = ahora.strftime('%H:%M:%S') if formato_24h else ahora.strftime('%I:%M:%S %p')
    fecha_str = ahora.strftime('%A %d %B %Y')

    # Actualizar etiquetas
    etiqueta_hora.config(text=hora_str)
    etiqueta_fecha.config(text=fecha_str)

    # Cambiar fondo según la hora del día
    hora_actual = ahora.hour
    if 6 <= hora_actual < 12:
        color_fondo = "#000000"  # Mañana
    elif 12 <= hora_actual < 18:
        color_fondo = "#000000"  # Tarde
    else:
        color_fondo = "#000000"  # Noche

    ventana.configure(bg=color_fondo)
    etiqueta_hora.configure(bg=color_fondo)
    etiqueta_fecha.configure(bg=color_fondo)
    boton_formato.configure(bg=color_fondo)

    # Reproducir sonido exactamente al comenzar una nueva hora
    if ahora.minute == 0 and ahora.second == 0:
        if ultima_hora_en_punto != ahora.hour:
            reproducir_sonido()
            ultima_hora_en_punto = ahora.hour

    ventana.after(1000, actualizar_reloj)
def mostrar_calendario():
    top = tk.Toplevel(ventana)
    top.title("Calendario")
    top.geometry("300x300")
    hoy = datetime.now()
    calendario_actual = calendar.TextCalendar().formatmonth(hoy.year, hoy.month)
    etiqueta_calendario = tk.Label(top, text=calendario_actual, font=("Arial", 12), bg="black", fg="white", justify="left")
    etiqueta_calendario.pack(pady=20)

def cambiar_formato():
    global formato_24h
    formato_24h = not formato_24h

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital Personalizado")
ventana.geometry("400x250")
ventana.resizable(False, False)

# Etiqueta hora
etiqueta_hora = tk.Label(ventana, font=('Arial', 50, 'bold'), fg='red')
etiqueta_hora.pack(pady=5)

# Etiqueta fecha
etiqueta_fecha = tk.Label(ventana, font=('Calibri', 23),fg='red')
etiqueta_fecha.pack()
#Temporizador
boton_formato = tk.Button(ventana, text="Cambiar formato", command=cambiar_formato, font=('Arial', 12), bg='black', fg='red')
boton_formato.pack(pady=10)
actualizar_reloj()
# Ejecutar la app
ventana.mainloop()