from models.contenedor import Contenedor
from models.tipo_entidad import TipoEntidad

class Estanteria(Contenedor):

    def __init__(self, objetos=None):
        super().__init__(TipoEntidad.ESTANTERIA, objetos)

        self._limpia = True
    
    def esta_limpia(self):
        return self._limpia
    
    def limpiar(self):
        self._limpia = True

    def ensuciar(self):
        self._limpia = False

    def __repr__(self):
        return (f"{[o.nombre for o in self._objetos]}")