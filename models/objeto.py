from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad

class Objeto(Entidad):

    def __init__(self, nombre):
        super().__init__(TipoEntidad.OBJETO)
        
        self.nombre = nombre

    def __repr__(self):
        return self.nombre