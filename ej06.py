"""Ejercicio 6 - Cuenta corriente en un comercio."""


def formato_gs(monto):
    return f"{monto:,.0f}".replace(",", ".") + " Gs."


class CuentaCliente:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def acreditar(self, monto):
        if monto <= 0:
            print(f"  [AVISO] Monto inválido ({formato_gs(monto)}), debe ser positivo.")
            return False
        self._saldo += monto
        print(f"  Se acreditaron {formato_gs(monto)}")
        return True

    def consumir(self, monto):
        if monto <= 0:
            print(f"  [AVISO] Monto inválido ({formato_gs(monto)}), debe ser positivo.")
            return False
        if monto > self._saldo:
            print(
                f"  [AVISO] Compra rechazada de {formato_gs(monto)} - "
                f"saldo insuficiente."
            )
            return False
        self._saldo -= monto
        print(f"  Compra registrada por {formato_gs(monto)}")
        return True

    def __str__(self):
        return f"Cuenta de {self.titular} | Saldo: {formato_gs(self._saldo)}"


if __name__ == "__main__":
    cuenta = CuentaCliente("Ana Villalba")
    print(cuenta)
    operaciones = [
        ("acreditar", 200000),
        ("consumir", 75000),
        ("consumir", 300000),   # se rechaza por falta de fondos
        ("acreditar", -5000),   # monto inválido
        ("acreditar", 50000),
        ("consumir", 175000),
    ]
    for i, (op, monto) in enumerate(operaciones, start=1):
        print(f"Operación {i}: {op} {formato_gs(monto)}")
        getattr(cuenta, op)(monto)
        print(f"  -> {cuenta}")
