from models.item_pedido import ItemPedido

class Pedido():
    
    def __init__(self, mesa):
        self._mesa_actual = mesa
        self._valor = 0
        self._items = []

    def cantidad_items(self):
        return len(self._items)

    def agregar_item(self, item):
        if (item is None) or (item in self._items):
            return False
        self._items.append(item)
        self._valor += item.valor()
        return True
    
    def quitar_item(self, item):
        if (item is None) or (not item in self._items):
            return False
        self._items.remove(item)
        self._valor -= item.valor()
        return True
    
    def mesa_actual(self):
        return self._mesa_actual
    
    def valor(self):
        return self._valor

    def cambiar_mesa(self, mesa):
        self._mesa_actual = mesa

    def __repr__(self):
        return (
            "\n".join([f"{i.nombre}: ${i.valor()}" for i in self._items]) + \
            f"\n--------------------------------------" + \
            f"\nTOTAL: ${self._valor}"
        )