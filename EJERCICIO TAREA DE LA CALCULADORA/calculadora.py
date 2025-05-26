import tkinter as tk

def calcular_suma():
    print(entrada)
    expresion = entrada.get()
    print(expresion)
    try:
        if all(char in "0123456789+*-/" for char in expresion):
            resultado = eval(expresion)
            resultado_var.set(f"Resultado: {resultado}")
        else:
            resultado_var.set("Syntaxis Error")
    except:
        resultado_var.set("Error en la expresión")
def limpiar():
    entrada.set("")
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora de Operaciones")
ventana.geometry("300x200")

entrada = tk.StringVar()
resultado_var = tk.StringVar()

tk.Label(ventana, text="Ingrese números a sumar (ej: 2+3+5 o 4*4, 6/2):").pack(pady=10)
tk.Entry(ventana, textvariable=entrada, font=("Arial", 14), justify="center").pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular_suma).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

tk.Label(ventana, textvariable=resultado_var, font=("Arial", 14), fg="blue").pack(pady=10)

ventana.mainloop()