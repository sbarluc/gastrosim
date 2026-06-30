from models.item_pedido import ItemPedido

class Pedido():
    
    def __init__(self, mesa):
        self._mesa_actual = mesa
        self._valor = 0
        self._items = []

    def cantidad_items(self):
        return len(self._items)

    def agregar_item(self, menu, nombre):
        item = ItemPedido(menu, nombre)
        if item is not None:
            self._items.append(item)
            self._valor += item.valor()
            return True
        return False
    
    def quitar_item(self, nombre):
        for item in self._items:
            if item.nombre == nombre:
                self._items.remove(item)
                self._valor -= item.valor()
                return True
        return False
    
    def agregar_descuento(self, valor):
        item_descuento = ItemPedido().descuento_neto(valor)
        self._items.append(item_descuento)
        self._valor -= valor
    
    def mesa_actual(self):
        return self._mesa_actual
    
    def valor(self):
        return self._valor

    def cambiar_mesa(self, mesa):
        self._mesa_actual = mesa