menu = {
    1: "dia de hoy",
    2: "numero al azar",
    3: "saludo",
    4: "salir"
}
print ("bienvenido al menu")
print ("ingrese un numero del 1 al 4")
while True:
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
        import datetime
        hoy = datetime.date.today()
        print("hoy es: ", hoy)
    if opcion == 2:
        import random
        numero = random.randint(1, 100)
        print("escoji un numero al azar por ti : " + str(numero))
    if opcion == 3:
        print("Buenos Dias Crack")
    if opcion == 4:
        break
print ("gracias Por Su Tiempo")    
    

