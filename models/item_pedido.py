from models.entidad import Entidad

class ItemPedido(Entidad):

    def __init__(self, nombre="", valor=0):
        self.nombre = nombre
        self._valor = valor
        self._entregado = False
        self._fue_pedido = False

    def fue_entregado(self):
        return self._entregado

    def fue_pedido(self):
        return self._fue_pedido
    
    def valor(self):
        return self._valor
    
    def entregar(self):
        self._entregado = True

    def pedir(self):
        self._fue_pedido = True

    @classmethod
    def desde_menu(cls, menu, nombre):
        precio = menu.precio(nombre)
        if precio is None:
            return None
        return cls(nombre, precio)