from models.entidad import Entidad

class Objeto(Entidad):

    def __init__(self, nombre):
        super().__init__()
        
        self.nombre = nombre

    def __repr__(self):
        return self.nombre