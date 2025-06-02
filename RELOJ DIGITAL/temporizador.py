import tkinter as tk
class Temporizador:
    def __init__(self, master):
        self.master = master
        self.master.title("Temporizador")
        self.tiempo = 0
        self.running = False

        self.label = tk.Label(master, text="00:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, width=5, font=("Arial", 24), justify='center')
        self.entry.pack()
        self.entry.insert(0, "60")  # segundos por defecto

        self.start_btn = tk.Button(master, text="Iniciar", command=self.iniciar)
        self.start_btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_btn = tk.Button(master, text="Detener", command=self.detener)
        self.stop_btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_btn = tk.Button(master, text="Reiniciar", command=self.reiniciar)
        self.reset_btn.pack(side=tk.LEFT, padx=10, pady=10)

    def actualizar_tiempo(self):
        if self.running and self.tiempo > 0:
            mins, secs = divmod(self.tiempo, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.tiempo -= 1
            self.master.after(1000, self.actualizar_tiempo)
        elif self.tiempo == 0:
            self.label.config(text="00:00")
            self.running = False

    def iniciar(self):
        if not self.running:
            try:
                self.tiempo = int(self.entry.get())
            except ValueError:
                self.tiempo = 60
            self.running = True
            self.actualizar_tiempo()

    def detener(self):
        self.running = False

    def reiniciar(self):
        self.running = False
        try:
            self.tiempo = int(self.entry.get())
        except ValueError:
            self.tiempo = 60
        mins, secs = divmod(self.tiempo, 60)
        self.label.config(text=f"{mins:02d}:{secs:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Temporizador(root)
    root.mainloop()