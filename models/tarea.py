from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad

class Tarea(Entidad):

    def __init__(self, tipo, duracion):
        super().__init__(TipoEntidad.TAREA)
        
        self.tipo = tipo
        self.duracion_total = duracion
        self.duracion_restante = duracion
        self.estado = "PENDIENTE"

    def iniciar(self):
        self.estado = "EN_PROGRESO"

    def avanzar(self):
        if self.esta_en_progreso():
            self.duracion_restante -= 1
        if self.duracion_restante == 0:
            self.estado = "COMPLETADA"

    def esta_pendiente(self):
        return self.estado == "PENDIENTE"
    
    def esta_completada(self):
        return self.estado == "COMPLETADA"
    
    def esta_en_progreso(self):
        return self.estado == "EN_PROGRESO"