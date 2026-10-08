"""Ejercicio 8 - Lista de reproducción de canciones."""


def formato_duracion(segundos):
    minutos, seg = divmod(segundos, 60)
    return f"{minutos}:{seg:02d}"


class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion_segundos

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({formato_duracion(self.duracion)})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion
        return total

    def __str__(self):
        lineas = [f"Lista: {self.nombre}"]
        for i, c in enumerate(self._canciones, start=1):
            lineas.append(f"  {i}. {c}")
        lineas.append(
            f"Duración total: {formato_duracion(self.duracion_total())} "
            f"({len(self._canciones)} canciones)"
        )
        return "\n".join(lineas)


if __name__ == "__main__":
    lista = ListaReproduccion("Para el viaje")
    lista.agregar(Cancion("Bohemian Rhapsody", "Queen", 355))
    lista.agregar(Cancion("Hotel California", "Eagles", 391))
    lista.agregar(Cancion("De Música Ligera", "Soda Stereo", 211))
    lista.agregar(Cancion("Rayando el Sol", "Maná", 261))
    print(lista)
