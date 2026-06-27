from models.contenedor import Contenedor
from models.tipo_entidad import TipoEntidad

class Inventario(Contenedor):

    def __init__(self, objetos=None, carga_max=float("inf")):
        super().__init__(TipoEntidad.INVENTARIO, objetos, carga_max)
    
    def __repr__(self):
        return (f"{[o.nombre for o in self._objetos]}")