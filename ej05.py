"""Ejercicio 5 - Vehículo de una agencia."""


class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        precio_fmt = f"{self.precio:,.0f}".replace(",", ".")
        return f"{self.marca} {self.modelo} {self.anio} — {precio_fmt} Gs."

    def __str__(self):
        return self.descripcion_comercial()


if __name__ == "__main__":
    autos = [
        Vehiculo("Toyota", "Corolla", 2020, 95000000),
        Vehiculo("Kia", "Sportage", 2022, 180000000),
        Vehiculo("Nissan", "Frontier", 2018, 125000000),
    ]
    for auto in autos:
        print(auto.descripcion_comercial())
