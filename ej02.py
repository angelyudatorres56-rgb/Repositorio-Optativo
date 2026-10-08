"""Ejercicio 2 - Producto de almacén."""


def formato_gs(monto):
    """Devuelve un monto con separador de miles paraguayo: 1.250.000 Gs."""
    return f"{monto:,.0f}".replace(",", ".") + " Gs."


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_total_stock(self):
        return self.precio * self.stock

    def __str__(self):
        return (
            f"{self.nombre} | Precio: {formato_gs(self.precio)} | "
            f"Stock: {self.stock} u."
        )


if __name__ == "__main__":
    productos = [
        Producto("Arroz 1 kg", 8500, 120),
        Producto("Aceite 900 ml", 14000, 60),
        Producto("Yerba mate 500 g", 18500, 45),
    ]
    for p in productos:
        print(p)
        print(f"   Valor total en stock: {formato_gs(p.valor_total_stock())}")
