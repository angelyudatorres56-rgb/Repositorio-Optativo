"""Ejercicio 10 - Carrito de compras (reutiliza Producto del ejercicio 2)."""

from ej02 import Producto, formato_gs


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return (
            f"{self.producto.nombre} x{self.cantidad} "
            f"({formato_gs(self.producto.precio)} c/u) = "
            f"{formato_gs(self.subtotal())}"
        )


class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self._items = []

    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            print("  [AVISO] La cantidad debe ser positiva.")
            return
        self._items.append(Item(producto, cantidad))

    def total(self):
        return sum(item.subtotal() for item in self._items)

    def mostrar_detalle(self):
        print(f"Carrito de {self.cliente}")
        for item in self._items:
            print(f"  - {item}")
        print(f"TOTAL A PAGAR: {formato_gs(self.total())}")

    def __str__(self):
        return f"Carrito de {self.cliente}: {len(self._items)} ítems"


if __name__ == "__main__":
    auriculares = Producto("Auriculares Bluetooth", 180000, 25)
    mouse = Producto("Mouse inalámbrico", 95000, 40)
    pendrive = Producto("Pendrive 64 GB", 45000, 100)

    carrito = Carrito("Valeria Núñez")
    carrito.agregar(auriculares, 1)
    carrito.agregar(mouse, 2)
    carrito.agregar(pendrive, 3)
    carrito.mostrar_detalle()
