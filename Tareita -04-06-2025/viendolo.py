class CuentaBancaria:
    # Mensaje de bienvenida (se muestra una vez al definir la clase)
    print("Bienvenido al sistema de gestión de cuentas bancarias.\nPor favor, complete los siguientes datos para crear su cuenta.")
    
    def __init__(self, titular, saldo):
        # Atributos encapsulados (privados)
        self.__titular = titular
        self.__saldo = saldo
        print(f"""
Cuenta creada exitosamente.
Titular: {self.__titular}
Saldo: ARS${self.__saldo}
***""")
    
    def depositar(self, monto):
        # Verifica que el monto sea numérico
        if isinstance(monto, (int, float)):
            if monto > 0:
                self.__saldo += monto
                print(f"Se realizó el depósito de ARS${monto} correctamente. Saldo actual: ARS${self.__saldo}")
            else:
                print("El monto ingresado no es válido. Debe depositar un monto positivo.")
        else:
            print("Error. El monto a depositar debe ser numérico.")
    
    def retirar(self, monto):
        if isinstance(monto, (int, float)):
            if monto > 0:
                if monto <= self.__saldo:
                    self.__saldo -= monto
                    print(f"Se realizó el retiro correctamente. Saldo actual: ARS${self.__saldo}")
                else:
                    print("Fondos insuficientes.")
            else:
                print("El monto a retirar debe ser mayor a cero.")
        else:
            print("Monto incorrecto. El valor que desea retirar debe ser un número.")
    
    def consultar_saldo(self):
        print(f"Su saldo actual es de ARS${self.__saldo}")
    
    def consultar_titular(self):
        print(f"El propietario de la cuenta es {self.__titular}")


# Bloque de prueba (sólo se ejecuta si se corre este archivo de forma directa)
if __name__ == '__main__':
    # Se crea una cuenta de ejemplo
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    
    # Se realizan operaciones de depósito y retiro
    cuenta.depositar(500)
    cuenta.retirar(200)
    
    # Se consulta el saldo y el titular de la cuenta
    cuenta.consultar_saldo()
    cuenta.consultar_titular()