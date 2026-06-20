from models.contenedor import Contenedor

class Estanteria(Contenedor):
    siguiente_id = 1

    def __init__(self, objetos=None):
        super().__init__(objetos)

        self.id = Estanteria.siguiente_id
        Estanteria.siguiente_id += 1

        self.limpia = True
    
    def esta_limpia(self):
        return self.limpia
    
    def limpiar(self):
        self.limpia = True

    def ensuciar(self):
        self.limpia = False

    def __repr__(self):
        return (
            f"      |Estanteria[{self.id}] - {'limpia' if self.esta_limpia() else 'sucia'}\n"
            f"      |objetos: (?/?) | {[o.nombre for o in self.objetos]}\n"
        )