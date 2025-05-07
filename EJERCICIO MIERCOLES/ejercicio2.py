# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Para crear una lista con los números primos entre 1 y 1000
numeros_primos = [num for num in range(1, 1001) if es_primo(num)]

# Para mostrar los números primos
print("Números primos entre 1 y 1000:")
print(numeros_primos)