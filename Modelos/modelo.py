class Cuenta:
    def __init__(self, numero_cuenta: int, documento_id: int, nombre: str, saldo: float):
        """Constructor de la cuenta bancaria"""
        self.__numero_cuenta = numero_cuenta # Atributo privado (sin mutador)
        self.documento_id = documento_id
        self.nombre = nombre
        self.saldo = saldo

    def depositar_dinero(self, cantidad: float):
        """Deposita dinero aplicando una retención del 19%"""
        retencion = cantidad * 0.19
        self.saldo += cantidad - retencion
        print(f"Se ha depositado ${cantidad:.2f}, con retención de ${retencion:.2f}. Saldo actual: ${self.saldo:.2f}")

    def retirar_dinero(self, cantidad: float):
        """Retira dinero si hay suficiente saldo"""
        if cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Se ha retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

