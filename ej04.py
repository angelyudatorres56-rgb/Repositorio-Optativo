"""Ejercicio 4 - Libro de una biblioteca."""


class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        situacion = "Disponible" if self.disponible else "Prestado"
        return f"«{self.titulo}» de {self.autor} - {situacion}"


if __name__ == "__main__":
    libro1 = Libro("Hijo de hombre", "Augusto Roa Bastos", True)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", False)
    print(libro1)
    print(libro2)
