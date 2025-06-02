import tkinter as tk
import time
from datetime import datetime
import platform

# Solo importar winsound si estamos en Windows
if platform.system() == "Windows":
    import winsound

# Variable global para formato de hora
formato_24h = False

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
        color_fondo = '#ADD8E6'  # Mañana
    elif 12 <= hora_actual < 18:
        color_fondo = '#FFD580'  # Tarde
    else:
        color_fondo = '#2F4F4F'  # Noche

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

def cambiar_formato():
    global formato_24h
    formato_24h = not formato_24h

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital Personalizado")
ventana.geometry("400x200")
ventana.resizable(False, False)

# Etiqueta hora
etiqueta_hora = tk.Label(ventana, font=('Arial', 40, 'bold'), fg='black')
etiqueta_hora.pack(pady=5)

# Etiqueta fecha
etiqueta_fecha = tk.Label(ventana, font=('Calibri', 23),fg='black')
etiqueta_fecha.pack()

# Botón para cambiar formato
boton_formato = tk.Button(ventana, text="Cambiar Formato 12h/24h", command=cambiar_formato, font=('Arial', 12))
boton_formato.pack(pady=10)

# Inicializar última hora para controlar el sonido
ultima_hora_en_punto = -1

# Iniciar el reloj
actualizar_reloj()

# Ejecutar la app
ventana.mainloop()