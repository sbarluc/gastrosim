from models.entidad import Entidad
from models.estado_item_pedido import EstadoItemPedido

class ItemPedido(Entidad):

    def __init__(self, nombre="", valor=0):
        self.nombre = nombre
        self._valor = valor
        self._estados = set()
    
#------------------------------------------------------------------------------------

    def preparar_para_pedir(self):
        return self._estados.add(EstadoItemPedido.PARA_PEDIR)
    
    def esta_para_pedir(self):
        return EstadoItemPedido.PARA_PEDIR in self._estados
    
    def pedir(self):
        if self.esta_para_pedir():
            self._estados.remove(EstadoItemPedido.PARA_PEDIR) 
            return self._estados.add(EstadoItemPedido.ESPERANDO)

    def fue_pedido(self):
        return EstadoItemPedido.ESPERANDO in self._estados
    
#-------------------------------------------------------------------------------------
    
    def entregar(self):
        return self._estados.add(EstadoItemPedido.ENTREGADO)
    
    def fue_entregado(self):
        return EstadoItemPedido.ENTREGADO in self._estados

#-------------------------------------------------------------------------------------

    def sin_estado(self):
        return not self._estados

    def valor(self):
        return self._valor

    @classmethod
    def desde_menu(cls, menu, nombre):
        precio = menu.precio(nombre)
        if precio is None:
            return None
        return cls(nombre, precio)