import tkinter as tk
from tkinter import messagebox
import sqlite3

class TodoApp:
    """
    Clase principal para la aplicación de Lista de Tareas.
    Engloba toda la lógica de la interfaz y la base de datos.
    """
    def __init__(self, root):
        self.root = root
        self.configurar_ventana()
        
        self.conn = None
        self.cursor = None
        self.lista_de_tareas_actual = []
        
        self.inicializar_y_conectar_db()
        self.crear_widgets()
        self.cargar_tareas()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def configurar_ventana(self):
        """Configura las propiedades principales de la ventana."""
        self.root.title("Mi lista de tareas (Proyecto TKinter)")
        self.root.geometry("550x650")
        self.root.configure(bg="#f0f0f0")
        self.root.minsize(450, 550)

    def inicializar_y_conectar_db(self):
        """
        Inicializa la tabla de la base de datos si no existe
        y establece una conexión persistente.
        """
        db_name = "tareas_final.db"
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY,
                    descripcion TEXT NOT NULL,
                    completada BOOLEAN DEFAULT 0 NOT NULL CHECK (completada IN (0, 1))
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo conectar o inicializar la base de datos: {e}")
            self.root.destroy()

    def on_closing(self):
        """Cierra la conexión a la base de datos de forma segura al salir."""
        if self.conn:
            self.conn.close()
        self.root.destroy()

    def crear_widgets(self):
        """Crea y organiza todos los elementos de la interfaz gráfica."""
        # --- Fuentes y Colores ---
        font_titulo = ("Arial", 24, "bold")
        font_normal = ("Arial", 12)
        color_fondo = "#f0f0f0"
        color_cabecera = "#4a90e2"
        color_texto_cabecera = "#ffffff"
        color_boton_add = "#27ae60"
        color_boton_del = "#c0392b"
        color_lista = "#ffffff"

        # --- Marco de la Cabecera ---
        header_frame = tk.Frame(self.root, bg=color_cabecera, padx=20, pady=20)
        header_frame.pack(fill="x")
        
        titulo_label = tk.Label(header_frame, text="Lista de Tareas", font=font_titulo, bg=color_cabecera, fg=color_texto_cabecera)
        titulo_label.pack()
        
        # --- Marco para la Entrada de Tareas ---
        entry_frame = tk.Frame(self.root, bg=color_fondo, pady=10)
        entry_frame.pack(fill="x", padx=20)

        self.task_entry = tk.Entry(entry_frame, width=45, font=font_normal, relief="solid", borderwidth=1)
        self.task_entry.pack(side="left", fill="x", expand=True)
        
        add_button = tk.Button(entry_frame, text="Añadir", command=self.anadir_tarea, bg=color_boton_add, fg="white", font=font_normal, relief="flat", padx=10)
        add_button.pack(side="left", padx=(10, 0))

        # --- Marco para la Lista de Tareas ---
        list_frame = tk.Frame(self.root, bg=color_fondo)
        list_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.tasks_listbox = tk.Listbox(list_frame, height=15, font=font_normal, selectbackground="#a6a6a6", bg=color_lista, relief="solid", borderwidth=1, activestyle='none')
        self.tasks_listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.tasks_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)

        # --- Marco para los Botones de Acción ---
        actions_frame = tk.Frame(self.root, bg=color_fondo, pady=10)
        actions_frame.pack(fill="x", padx=20)
        
        complete_button = tk.Button(actions_frame, text="Completar", command=self.marcar_completada, font=font_normal, relief="flat", bg="#3498db", fg="white")
        complete_button.pack(side="left", expand=True, fill="x", padx=5)

        pending_button = tk.Button(actions_frame, text="Pendiente", command=self.marcar_pendiente, font=font_normal, relief="flat", bg="#f39c12", fg="white")
        pending_button.pack(side="left", expand=True, fill="x", padx=5)
        
        delete_button = tk.Button(actions_frame, text="Eliminar", command=self.eliminar_tarea, font=font_normal, bg=color_boton_del, fg="white", relief="flat")
        delete_button.pack(side="left", expand=True, fill="x", padx=5)
    
    def cargar_tareas(self):
        """Carga las tareas desde la BD y las refresca en la lista visual."""
        self.tasks_listbox.delete(0, tk.END)
        try:
            self.cursor.execute("SELECT id, descripcion, completada FROM tareas ORDER BY id")
            self.lista_de_tareas_actual = self.cursor.fetchall()
            
            for i, row in enumerate(self.lista_de_tareas_actual):
                _task_id, descripcion, completada = row
                
                # Mejora visual: Añade un prefijo si la tarea está completada
                display_text = f"[✓] {descripcion}" if completada else descripcion
                self.tasks_listbox.insert(tk.END, display_text)
                
                if completada:
                    # Aplica un color gris a la tarea completada como indicador visual
                    self.tasks_listbox.itemconfig(i, {'fg': 'gray'})
                else:
                    # Asegura que las tareas pendientes tengan el color por defecto
                    self.tasks_listbox.itemconfig(i, {'fg': 'black'})
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudieron cargar las tareas: {e}")

    def anadir_tarea(self):
        """Añade una nueva tarea a la BD y refresca la lista."""
        descripcion = self.task_entry.get().strip()
        if not descripcion:
            messagebox.showwarning("Entrada Vacía", "La descripción de la tarea no puede estar vacía.")
            return
        
        try:
            self.cursor.execute("INSERT INTO tareas (descripcion, completada) VALUES (?, ?)", (descripcion, False))
            self.conn.commit()
            self.task_entry.delete(0, tk.END)
            self.cargar_tareas()
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo añadir la tarea: {e}")

    def _get_selected_task_id(self):
        """Helper para obtener el ID de la tarea seleccionada en la lista."""
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            return self.lista_de_tareas_actual[selected_task_index][0]
        except IndexError:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona una tarea de la lista.")
            return None

    def _update_task_status(self, task_id, status):
        """Helper para actualizar el estado (completada/pendiente) de una tarea."""
        if not task_id:
            return
        try:
            self.cursor.execute("UPDATE tareas SET completada = ? WHERE id = ?", (status, task_id))
            self.conn.commit()
            self.cargar_tareas()
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo actualizar la tarea: {e}")

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada (completada=True)."""
        task_id = self._get_selected_task_id()
        self._update_task_status(task_id, True)

    def marcar_pendiente(self):
        """Marca la tarea seleccionada como pendiente (completada=False)."""
        task_id = self._get_selected_task_id()
        self._update_task_status(task_id, False)

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la BD."""
        task_id = self._get_selected_task_id()
        if not task_id:
            return
            
        if messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que quieres eliminar esta tarea?"):
            try:
                self.cursor.execute("DELETE FROM tareas WHERE id = ?", (task_id,))
                self.conn.commit()
                self.cargar_tareas()
            except sqlite3.Error as e:
                messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar la tarea: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()