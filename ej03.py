"""Ejercicio 3 - Empleado y su sueldo."""

MESES_POR_ANIO = 12


def formato_gs(monto):
    return f"{monto:,.0f}".replace(",", ".") + " Gs."


class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self, con_aguinaldo=True):
        """Salario por 12 meses; con aguinaldo suma un mes adicional."""
        meses = MESES_POR_ANIO + (1 if con_aguinaldo else 0)
        return self.salario_mensual * meses

    def __str__(self):
        return (
            f"{self.nombre} - {self.cargo} | "
            f"Salario mensual: {formato_gs(self.salario_mensual)}"
        )


if __name__ == "__main__":
    empleados = [
        Empleado("Laura Páez", "Contadora", 4500000),
        Empleado("Diego Ramírez", "Vendedor", 2800000),
    ]
    for e in empleados:
        print(e)
        print(f"   Anual sin aguinaldo: {formato_gs(e.salario_anual(False))}")
        print(f"   Anual con aguinaldo: {formato_gs(e.salario_anual())}")
