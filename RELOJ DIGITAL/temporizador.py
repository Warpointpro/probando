import tkinter as tk

class CuentaAtras(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.controlesTiempo = tk.Frame(self)
        self.controlesTiempo.pack(side=tk.TOP)
        
        # Etiqueta de "Horas" y spinbox en rojo
        self.labelHora = tk.Label(self.controlesTiempo, text="Horas", width=8, fg="black")
        self.labelHora.pack(side=tk.LEFT)
        self.cajaHora = tk.Spinbox(self.controlesTiempo, from_=0, to=5, fg="black")
        self.cajaHora.pack(side=tk.LEFT)
        
        # Etiqueta de "Minutos" y spinbox en rojo
        self.labelMinuto = tk.Label(self.controlesTiempo, text="Minutos", width=8, fg="black")
        self.labelMinuto.pack(side=tk.LEFT)
        self.cajaMinuto = tk.Spinbox(self.controlesTiempo, from_=0, to=40, fg="black")
        self.cajaMinuto.pack(side=tk.LEFT)
        
        # Etiqueta de "Segundos" y spinbox en rojo
        self.labelSegundo = tk.Label(self.controlesTiempo, text="Segundos", width=8, fg="black")
        self.labelSegundo.pack(side=tk.LEFT)
        self.cajaSegundo = tk.Spinbox(self.controlesTiempo, from_=0, to=50, fg="black")
        self.cajaSegundo.pack(side=tk.LEFT)
        
        self.frCuenta = tk.Frame(self)
        self.frCuenta.pack(side=tk.BOTTOM)
        # Aquí se muestra la cuenta regresiva; añadimos fg="red"
        self.etiquetaCuenta = tk.Label(self, text="00:00:00", font=('Courier New', 70, 'bold'), bg="black", fg="red")
        self.etiquetaCuenta.pack()
        
        self.restante = 0
        if hasattr(self, 'after_id'):
            self.after_cancel(self.after_id)
        self.botones = tk.Frame(self)
        self.botones.pack(side=tk.BOTTOM)
        self.btnIniciar = tk.Button(self.botones, text="Iniciar", command=self.iniciar)
        self.btnIniciar.pack(side=tk.LEFT)
        self.btnDetener = tk.Button(self.botones, text="Detener", command=self.detener, state=tk.DISABLED)
        self.btnDetener.pack(side=tk.LEFT)
        self.btnIniciar["state"] = tk.NORMAL
        self.btnDetener["state"] = tk.DISABLED

    def aHoras(self, segundos):
        segundos = segundos % (24 * 3600)
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        return "%02d:%02d:%02d" % (horas, minutos, segundos)

    def aSegundos(self, hora):
        h, m, s = hora.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def cuenta(self, restante = None):
        if restante is not None:
            self.restante = restante

        if self.restante <= 0:
            mensajeFinal = "00:00:00"
            self.etiquetaCuenta.configure(text=mensajeFinal)
            self.escribirAarchivo(mensajeFinal)
            self.btnIniciar["state"] = tk.NORMAL
            self.btnDetener["state"] = tk.DISABLED
            self.sonidoFinal()
        else:
            horaActual = self.aHoras(self.restante)
            self.etiquetaCuenta.configure(text=horaActual)
            self.escribirAarchivo(horaActual)
            self.restante = self.restante - 1
            self.after_id = self.after(1000, self.cuenta)

    def iniciar(self):
        total = self.aSegundos("{0}:{1}:{2}".format(self.cajaHora.get(), self.cajaMinuto.get(), self.cajaSegundo.get()))
        if total > 0:
            self.cuenta(total)
            self.btnIniciar["state"] = tk.DISABLED
            self.btnDetener["state"] = tk.NORMAL
            self.sonidoTicTac()

    def detener(self):
        self.restante = 0

    def escribirAarchivo(self, texto):
        archivo = open("cuenta.txt","w", encoding="utf-8")
        archivo.write(texto)
        archivo.close()

    def sonidoFinal(self):
        pass

    def sonidoTicTac(self):
        pass

if __name__ == "__main__":
    app = CuentaAtras()
    app.mainloop()