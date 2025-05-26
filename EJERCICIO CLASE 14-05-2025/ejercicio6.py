numero = int(input("ingrese un número: "))
suma = 0
while numero > 0:
    suma += numero % 10
    numero = numero // 10
print("La suma de los dígitos es:", suma)
