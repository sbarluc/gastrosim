from models.item_pedido import ItemPedido

class Pedido():
    
    def __init__(self, mesa, menu=None):
        self.menu = menu
        self._mesa_actual = mesa
        self.precio = 0
        self._items = []

    def _buscar_item(self, nombre):
        for item in self._items:
            if item.nombre == nombre:
                return item
        return None

    def cantidad_items(self):
        return len(self._items)

    def agregar_item(self, nombre):
        item = ItemPedido(self.menu, nombre)
        if item is not None:
            self._items.append(item)
            self.precio += item.precio
            return True
        return False
    
    def quitar_item(self, nombre):
        item = self._buscar_item(nombre)
        if item is not None:
            self._items.remove(item)
            self.precio -= item.precio
            return True
        return False
    
    def mesa_actual(self):
        return self._mesa_actual

    def cambiar_mesa(self, mesa):
        self._mesa_actual = mesa