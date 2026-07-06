from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad

class Tarea(Entidad):

    def __init__(self, tipo, duracion):
        super().__init__(TipoEntidad.TAREA)
        
        self.tipo = tipo
        self.duracion_total = duracion
        self.duracion_restante = duracion

    def esta_pendiente(self):
        return self.duracion_restante > 0