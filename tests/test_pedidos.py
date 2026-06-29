from models.mesa import Mesa
from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido
from models.pedido import Pedido

def test_menu_recibe_diccionario_de_precios():
    menu = Menu(dicc_precios)
    assert menu.precio("Croissant nutella") == 4000
    
def test_crear_item_desde_un_menu():
    menu = Menu(dicc_precios)
    item_pedido = ItemPedido(menu, "Croissant nutella")
    assert item_pedido.precio() == 4000

def test_pedido_para_mesa_comienza_vacio():
    mesa = Mesa(1)
    pedido = Pedido(mesa)
    assert pedido.cantidad_items() == 0
    assert pedido.precio() == 0
    assert pedido.mesa_actual() == mesa

def test_agregar_item_a_pedido_actualiza_el_precio_total():
    menu = Menu(dicc_precios)
    mesa = Mesa(1)
    pedido = Pedido(mesa, menu)
    pedido.agregar_item("Salmón a la plancha")
    assert pedido.cantidad_items() == 1
    assert pedido.precio() == 9800

def test_quitar_item_a_pedido_actualiza_el_precio_total():
    menu = Menu(dicc_precios)
    mesa = Mesa(1)
    pedido = Pedido(mesa, menu)
    pedido.agregar_item("Cafe con leche")
    pedido.agregar_item("Croissant nutella")
    pedido.quitar_item("Croissant nutella")
    assert pedido.precio() == 3000

def item_entregado_no_puede_ser_borrado():
    menu = Menu(dicc_precios)
    mesa = Mesa(1)
    pedido = Pedido(mesa, menu)
    pedido.agregar_item("Cafe con leche")
    pedido.agregar_item("Croissant nutella")
    pedido.entregar_item("Cafe con leche")
    assert not pedido.quitar_item("Cafe con leche")
    assert pedido.precio() == 7000

def test_pedido_cambia_de_mesa():
    mesa1 = Mesa(1)
    mesa2 = Mesa(1)
    pedido = Pedido(mesa1)
    pedido.cambiar_mesa(mesa2)
    assert pedido.mesa_actual() == mesa2