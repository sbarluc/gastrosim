from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad

class Objeto(Entidad):

    def __init__(self, nombre, peso=0):
        super().__init__(TipoEntidad.OBJETO, nombre=nombre)
        
        self.peso = peso

    def info(self):
        return f"{self.nombre}({self.peso}g)"