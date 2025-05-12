numero_magico = 4
numero= int(input("di un numero de 1 al 10"))
while numero <0 or numero >10:
   print ("ingrese un numero dentro del rango valido")
   numero= int(input("di un numero de 1 al 10"))
if numero == numero_magico:
   print ("felicidades lo adivinaste")
else:
   print ("te equivocaste, ups")
