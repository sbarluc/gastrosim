from models.contenedor import Contenedor

class Inventario(Contenedor):

    def __init__(self, objetos=None):
        super().__init__(objetos)
    
    def __repr__(self):
        return (f"{[o.nombre for o in self.objetos]}")