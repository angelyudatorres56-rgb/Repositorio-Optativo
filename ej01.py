"""Ejercicio 1 - Ficha de cliente."""


class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (
            "--- Ficha de cliente ---\n"
            f"Nombre  : {self.nombre}\n"
            f"Cédula  : {self.cedula}\n"
            f"Teléfono: {self.telefono}"
        )


if __name__ == "__main__":
    cliente1 = Cliente("María González", "4.123.456", "0981 123 456")
    cliente2 = Cliente("Carlos Benítez", "3.987.654", "0971 654 321")
    print(cliente1)
    print()
    print(cliente2)
