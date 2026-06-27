from models.menu import Menu
from data.test_menu import dicc_precios

class ItemPedido():
    
    def __init__(self, menu, nombre):
        self.nombre = nombre
        self.precio = menu.precio(nombre)
        self._entregado = False