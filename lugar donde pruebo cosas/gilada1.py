diccionario = {
	1: "lunes",
	2: "martes",
	3: "miercoles",
	4: "jueves",
	5: "viernes",
	6: "sabado",
	7: "domingo"
}
numero = int(input("dame un numero del 1 al 7"))
if numero in diccionario:
	print("el dia de la semana es:", diccionario [numero])
else:
	print("ingrese un valor valido")
	