"""Ejercicio 13 - Habitación de un hotel."""


def formato_gs(monto):
    return f"{monto:,.0f}".replace(",", ".") + " Gs."


class Habitacion:
    def __init__(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche
        self._ocupada = False

    @property
    def ocupada(self):
        return self._ocupada

    def ocupar(self):
        if self._ocupada:
            print(f"  [AVISO] La habitación {self.numero} ya está ocupada.")
            return False
        self._ocupada = True
        print(f"  Habitación {self.numero} ocupada.")
        return True

    def liberar(self):
        if not self._ocupada:
            print(f"  [AVISO] La habitación {self.numero} ya está libre.")
            return False
        self._ocupada = False
        print(f"  Habitación {self.numero} liberada.")
        return True

    def costo_estadia(self, noches):
        if noches <= 0:
            print("  [AVISO] Las noches deben ser un número positivo.")
            return 0
        return self.tarifa_noche * noches

    def __str__(self):
        estado = "Ocupada" if self._ocupada else "Libre"
        return (
            f"Hab. {self.numero} ({self.tipo}) | "
            f"{formato_gs(self.tarifa_noche)}/noche | {estado}"
        )


if __name__ == "__main__":
    hab = Habitacion(204, "Doble", 350000)
    print(hab)
    print("1) Ocupar la habitación:")
    hab.ocupar()
    print(f"   {hab}")
    print("2) Intentar ocuparla de nuevo:")
    hab.ocupar()
    print("3) Calcular el costo de una estadía de 3 noches:")
    print(f"   Costo: {formato_gs(hab.costo_estadia(3))}")
    print("4) Liberar la habitación:")
    hab.liberar()
    print(f"   {hab}")
