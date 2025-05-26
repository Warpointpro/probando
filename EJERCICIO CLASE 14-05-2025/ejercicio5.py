cadena = input("Introduce un cualquier palabra")
invertida = ""
for letra in cadena:
    invertida = letra + invertida
print("la cadena invertida es: ", invertida)
if cadena == invertida:
 print ("la palabra se lee igual del derecho y del reves")
else:
   print ("la palabra no se lee igual del derecho y del reves")

    