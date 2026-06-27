class ItemPedido():
    
    def __init__(self, menu, nombre):
        self.nombre = nombre
        self.precio = menu.precio(nombre)