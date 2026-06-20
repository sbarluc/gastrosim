from models.contenedor import Contenedor
class Mesa(Contenedor):

    def __init__(self, sillas, objetos=None):
        super().__init__(objetos)

        self.sillas = sillas

        self.clientes_sentados = []

        self.limpia = True

    def tiene_lugar(self):
        return len(self.clientes_sentados) < self.sillas

    def esta_ocupada(self):
        return len(self.clientes_sentados) > 0
    
    def esta_limpia(self):
        return self.limpia
    
    def ocupar_silla(self, cliente):
        if not self.tiene_lugar():
            return False
        self.clientes_sentados.append(cliente)
        return True

    def desocupar_silla(self, cliente):
        if not cliente in self.clientes_sentados:
            return False
        self.clientes_sentados.remove(cliente)
        return True
    
    def limpiar(self):
        self.limpia = True

    def ensuciar(self):
        self.limpia = False

    def cantidad_sentados(self):
        return len(self.clientes_sentados)

    def __repr__(self):
        return (
            f"      |Mesa[{self.id}] - {'limpia' if self.esta_limpia() else 'sucia'}\n"
            f"      |clientes sentados: {[f'Cliente[{c.id}]' for c in self.clientes_sentados]}\n" 
            f"      |objetos: (?/?) | {[o.nombre for o in self.objetos]}\n"
        )