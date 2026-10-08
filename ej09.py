"""Ejercicio 9 - Turnos de un consultorio."""


class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def marcar_atendido(self):
        self.estado = "atendido"

    def __str__(self):
        return f"{self.hora} - {self.paciente} [{self.estado}]"


class Agenda:
    def __init__(self, fecha):
        self.fecha = fecha
        self._turnos = []

    def agendar(self, turno):
        if any(t.hora == turno.hora for t in self._turnos):
            print(f"  [AVISO] Ya existe un turno a las {turno.hora}.")
            return False
        self._turnos.append(turno)
        print(f"  Turno agendado: {turno}")
        return True

    def pendientes(self):
        return [t for t in self._turnos if t.estado == "pendiente"]

    def listar_pendientes(self):
        print(f"Turnos pendientes del {self.fecha}:")
        pendientes = self.pendientes()
        if not pendientes:
            print("  (no quedan turnos pendientes)")
        for t in pendientes:
            print(f"  - {t}")


if __name__ == "__main__":
    agenda = Agenda("08/10/2026")
    t1 = Turno("Julia Acosta", "08:00")
    t2 = Turno("Pedro Gómez", "08:30")
    t3 = Turno("Sofía Ortiz", "09:00")
    t4 = Turno("Luis Duarte", "09:30")
    for t in (t1, t2, t3, t4):
        agenda.agendar(t)
    agenda.agendar(Turno("Raúl Meza", "09:00"))  # horario ocupado
    print()
    t1.marcar_atendido()
    t2.marcar_atendido()
    print("Se atendió a Julia Acosta y a Pedro Gómez.")
    print()
    agenda.listar_pendientes()
