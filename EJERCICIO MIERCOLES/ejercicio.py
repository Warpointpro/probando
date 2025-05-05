meses = { 
"01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}
fecha_iso = input("introducir la fecha en formato Iso AAAAMMDD")
mes = fecha_iso[4:6]
nombre_mes = meses.get(mes, "Mes no valido")
print("El mes es: ", nombre_mes)
