class CuentaBancaria:
    print("Bienvenido al sistema de gestión de cuentas bancarias. Por favor, complete los siguientes datos para crear su cuenta.")
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        print(f"""
Cuenta creada exitosamente.
Titular: [self._titular]
Saldo: ARS$[self._saldo]
***""")

    def depositar(self, monto):
        if type(monto) == int or type(monto) == float:
            if monto > 0:
                self._saldo += monto
                print(f"Se realizó el depósito de ARS$[monto] correctamente. Saldo actual: ARS$[self._saldo]")
            else:
                print("El monto ingresado no es válido. Debe depositar un monto positivo")
        else:
            print("Error. El monto a depositar debe ser numérico.")

    def retirar(self, monto):
        if type(monto) == int or type(monto) == float:
            if monto > 0:
                if monto <= self._saldo:
                    self._saldo -= monto
                    print(f"Se realizó el retiro correctamente. Saldo actual: ARS$[self._saldo]")
                else:
                    print("Fondos insuficientes.")
            else:
                print("El monto a retirar debe ser mayor a cero")
        else:
            print("Monto incorrecto. El valor que desea retirar debe ser un número")

    def consultar_saldo(self):
        print(f"Su saldo actual es de ARS$[self._saldo]")

    def consultar_titular(self):
        print(f"El propietario de la cuenta es [self._titular]")