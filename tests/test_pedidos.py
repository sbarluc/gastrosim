from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido

def test_menu_recibe_diccionario_de_precios():
    menu = Menu(dicc_precios)
    assert menu.precio("Croissant nutella") == 4000
    
def test_item_pedido_comienza_no_entregado():
    menu = Menu(dicc_precios)
    item_pedido = ItemPedido(menu, "Croissant nutella")
    assert item_pedido.precio == 4000
    assert not item_pedido._entregado