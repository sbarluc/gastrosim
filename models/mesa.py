from models.contenedor import Contenedor

class Mesa(Contenedor):

    def __init__(self, cantidad_sillas, objetos=None):
        super().__init__(objetos)

        self.cantidad_sillas = cantidad_sillas
        
        self._clientes_sentados = []
        self._limpia = True

    def tiene_lugar(self):
        return len(self._clientes_sentados) < self.cantidad_sillas

    def esta_ocupada(self):
        return len(self._clientes_sentados) > 0
    
    def esta_limpia(self):
        return self._limpia
    
    def ocupar_silla(self, cliente):
        if not self.tiene_lugar():
            return False
        
        self._clientes_sentados.append(cliente)
        return True

    def desocupar_silla(self, cliente):
        if not cliente in self._clientes_sentados:
            return False
        
        self._clientes_sentados.remove(cliente)
        return True
    
    def limpiar(self):
        self._limpia = True

    def ensuciar(self):
        self._limpia = False

    def cantidad_sentados(self):
        return len(self._clientes_sentados)
    
    def clientes_sentados(self):
        return self._clientes_sentados

    def __repr__(self):
        return (
            f"      |{self.id_gral} - Mesa[{self.id}] - {'limpia' if self.esta_limpia() else 'sucia'}{' - llena' if not self.tiene_lugar() else ''}\n"
            f"      |clientes sentados: {[c.nombre for c in self._clientes_sentados]}\n" 
            f"      |objetos: (?/?) | {[o.nombre for o in self._objetos]}\n"
        )