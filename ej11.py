"""Ejercicio 11 - Estudiante y sus materias."""


class Estudiante:
    NOTA_MINIMA_APROBACION = 3.0   # escala 1 a 5

    def __init__(self, nombre):
        self.nombre = nombre
        self._notas = {}

    def registrar_nota(self, materia, nota):
        if not 1 <= nota <= 5:
            print(f"  [AVISO] Nota inválida para {materia}: debe estar entre 1 y 5.")
            return
        self._notas[materia] = nota

    def promedio(self):
        if not self._notas:
            return 0
        return sum(self._notas.values()) / len(self._notas)

    def aprobo(self):
        return self.promedio() >= self.NOTA_MINIMA_APROBACION

    def __str__(self):
        lineas = [f"BOLETÍN - {self.nombre}"]
        for materia, nota in self._notas.items():
            lineas.append(f"  {materia:<22}: {nota}")
        condicion = "APROBADO" if self.aprobo() else "REPROBADO"
        lineas.append(f"Promedio: {self.promedio():.2f}")
        lineas.append(f"Condición final: {condicion}")
        return "\n".join(lineas)


if __name__ == "__main__":
    est1 = Estudiante("Andrea Fleitas")
    est1.registrar_nota("Python Lenguaje I", 5)
    est1.registrar_nota("Matemática", 4)
    est1.registrar_nota("Base de Datos", 3)
    est1.registrar_nota("Inglés Técnico", 6)  # nota inválida
    print(est1)
    print()
    est2 = Estudiante("Marcos Ibarra")
    est2.registrar_nota("Python Lenguaje I", 2)
    est2.registrar_nota("Matemática", 2)
    est2.registrar_nota("Base de Datos", 3)
    print(est2)
