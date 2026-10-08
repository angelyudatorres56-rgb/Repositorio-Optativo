"""Ejercicio 12 - Línea móvil con plan de datos."""


class LineaMovil:
    def __init__(self, titular, numero, gb_incluidos):
        self.titular = titular
        self.numero = numero
        self.gb_incluidos = gb_incluidos
        self._gb_consumidos = 0

    def gb_disponibles(self):
        return round(self.gb_incluidos - self._gb_consumidos, 2)

    def registrar_consumo(self, gb):
        if gb <= 0:
            print("  [AVISO] El consumo debe ser positivo.")
            return False
        if self.gb_disponibles() <= 0:
            print("  [AVISO] El paquete se agotó: no se puede seguir consumiendo.")
            return False
        if gb > self.gb_disponibles():
            print(
                f"  [AVISO] Consumo de {gb} GB excede lo disponible "
                f"({self.gb_disponibles()} GB): se consume el resto y el paquete se agotó."
            )
            self._gb_consumidos = self.gb_incluidos
            return True
        self._gb_consumidos += gb
        print(f"  Se consumieron {gb} GB.")
        if self.gb_disponibles() == 0:
            print("  [AVISO] El paquete se agotó.")
        return True

    def __str__(self):
        return (
            f"Línea {self.numero} ({self.titular})\n"
            f"     Plan: {self.gb_incluidos} GB | "
            f"Consumidos: {round(self._gb_consumidos, 2)} GB | "
            f"Quedan: {self.gb_disponibles()} GB"
        )


if __name__ == "__main__":
    linea = LineaMovil("Rosa Cardozo", "0985 111 222", 10)
    print(linea)
    for consumo in (2.5, 4, 3, 2, 1):
        print(f"Registrar consumo de {consumo} GB:")
        linea.registrar_consumo(consumo)
        print(f"  -> {linea}")
