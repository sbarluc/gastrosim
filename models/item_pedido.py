from models.entidad import Entidad

class ItemPedido(Entidad):
    
    def __init__(self, menu=None, nombre=""):
        self.nombre = nombre
        self._valor = menu.precio(nombre) if menu is not None else 0
        self._entregado = False

    def fue_entregado(self):
        return self._entregado
    
    def valor(self):
        return self._valor
    
    def entregar(self):
        self._entregado = True

    def descuento(self, valor):
        self.nombre = "Descuento"
        self._valor = valor
        return self