"""Ejercicio 7 - Control de stock con alertas."""


class ProductoStock:
    def __init__(self, nombre, precio, stock, stock_minimo):
        self.nombre = nombre
        self.precio = precio
        self._stock = stock
        self.stock_minimo = stock_minimo

    @property
    def stock(self):
        return self._stock

    def _verificar_minimo(self):
        if self._stock < self.stock_minimo:
            print(
                f"  [ALERTA] Reponer '{self.nombre}': stock {self._stock} "
                f"por debajo del mínimo ({self.stock_minimo})."
            )

    def ingresar_mercaderia(self, cantidad):
        if cantidad <= 0:
            print("  [AVISO] La cantidad a ingresar debe ser positiva.")
            return False
        self._stock += cantidad
        print(f"  Ingresaron {cantidad} unidades.")
        return True

    def vender(self, cantidad):
        if cantidad <= 0:
            print("  [AVISO] La cantidad a vender debe ser positiva.")
            return False
        if cantidad > self._stock:
            print(
                f"  [AVISO] Venta rechazada: se piden {cantidad} y solo hay "
                f"{self._stock} unidades."
            )
            return False
        self._stock -= cantidad
        print(f"  Se vendieron {cantidad} unidades.")
        self._verificar_minimo()
        return True

    def __str__(self):
        return (
            f"{self.nombre} | Stock: {self._stock} | Mínimo: {self.stock_minimo}"
        )


if __name__ == "__main__":
    p = ProductoStock("Fideos 500 g", 6500, 30, 10)
    print(p)
    print("Venta de 15:")
    p.vender(15)
    print(p)
    print("Venta de 8 (queda por debajo del mínimo):")
    p.vender(8)
    print(p)
    print("Venta de 20 (no alcanza el stock):")
    p.vender(20)
    print(p)
    print("Llega mercadería (+40):")
    p.ingresar_mercaderia(40)
    print(p)
