from models.item_pedido import ItemPedido

class Pedido():
    
    def __init__(self, mesa, menu=None):
        self.menu = menu
        self._mesa_actual = mesa
        self._precio = 0
        self._items = []

    def cantidad_items(self):
        return len(self._items)

    def agregar_item(self, nombre):
        item = ItemPedido(self.menu, nombre)
        if item is not None:
            self._items.append(item)
            self._precio += item.precio()
            return True
        return False
    
    def quitar_item(self, nombre):
        item = self._buscar_item_no_entregado(nombre)
        if item is not None:
            self._items.remove(item)
            self._precio -= item.precio()
            return True
        return False
    
    def mesa_actual(self):
        return self._mesa_actual
    
    def precio(self):
        return self._precio

    def cambiar_mesa(self, mesa):
        self._mesa_actual = mesa

    def _buscar_item_no_entregado(self, nombre):
        return next(
            (item for item in self._items 
             if (item.nombre == nombre and not item.fue_entregado()))
            , None
        )