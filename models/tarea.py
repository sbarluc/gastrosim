from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.estado_tarea import EstadoTarea

class Tarea(Entidad):

    def __init__(self, tipo, duracion):
        super().__init__(TipoEntidad.TAREA)
        
        self.tipo = tipo
        self.duracion_total = duracion
        self.duracion_restante = duracion
        self.estado = EstadoTarea.PENDIENTE

    def iniciar(self):
        self.estado = EstadoTarea.EN_PROGRESO

    def avanzar(self):
        if self.esta_en_progreso():
            self.duracion_restante -= 1
        if self.duracion_restante == 0:
            self.estado = EstadoTarea.COMPLETADA

    def cancelar(self):
        self.estado = EstadoTarea.CANCELADA

    def esta_pendiente(self):
        return self.estado == EstadoTarea.PENDIENTE
    
    def esta_en_progreso(self):
        return self.estado == EstadoTarea.EN_PROGRESO
    
    def esta_completada(self):
        return self.estado == EstadoTarea.COMPLETADA
    
    def esta_cancelada(self):
        return self.estado == EstadoTarea.CANCELADA