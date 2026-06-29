from models.entidad import Entidad

class ItemPedido(Entidad):
    
    def __init__(self, menu, nombre):
        self.nombre = nombre
        self._precio = menu.precio(nombre)
        self._entregado = False

    def fue_entregado(self):
        return self._entregado
    
    def precio(self):
        return self._precio
    
    def entregar(self):
        self._entregado = True