from models.entidad import Entidad

class ItemPedido(Entidad):

    def __init__(self, nombre="", valor=0):
        self.nombre = nombre
        self._valor = valor
        self._entregado = False

    def fue_entregado(self):
        return self._entregado
    
    def valor(self):
        return self._valor
    
    def entregar(self):
        self._entregado = True

    def desde_menu(self, menu):
        self._valor = 0
        precio = menu.precio(self.nombre)
        if precio:
            self._valor += precio
            return self
        return None