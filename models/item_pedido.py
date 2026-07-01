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

    @classmethod
    def desde_menu(cls, menu, nombre):
        precio = menu.precio(nombre)
        if precio is None:
            return None
        return cls(nombre, precio)