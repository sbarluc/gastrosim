from models.contenedor import Contenedor

class Estanteria(Contenedor):

    def __init__(self, objetos=None):
        super().__init__(objetos)

        self.limpia = True
    
    def esta_limpia(self):
        return self.limpia
    
    def limpiar(self):
        self.limpia = True

    def ensuciar(self):
        self.limpia = False

    def __repr__(self):
        return (
            f"      |{self.id_gral} - Estanteria[{self.id}] - {'limpia' if self.esta_limpia() else 'sucia'}\n"
            f"      |objetos: (?/?) | {[o.nombre for o in self.objetos]}\n"
        )