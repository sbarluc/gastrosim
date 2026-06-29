from models.mesa import Mesa
from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido
from models.pedido import Pedido

dicc_precios_1 = dicc_precios()
menu_1 = Menu(dicc_precios_1)
mesa_1 = Mesa(1)
mesa_2 = Mesa(1)

def test_menu_recibe_diccionario_de_precios():
    assert menu_1.precio("Croissant nutella") == dicc_precios_1["Croissant nutella"]
    
def test_crear_item_desde_un_menu():
    item_pedido = ItemPedido(menu_1, "Croissant nutella")
    assert item_pedido.precio() == dicc_precios_1["Croissant nutella"]

def test_pedido_para_mesa_comienza_vacio():
    pedido = Pedido(mesa_1)
    assert pedido.cantidad_items() == 0
    assert pedido.precio() == 0
    assert pedido.mesa_actual() == mesa_1

def test_agregar_item_a_pedido_actualiza_el_precio_total():
    pedido = Pedido(mesa_1, menu_1)
    pedido.agregar_item("Salmón a la plancha")
    assert pedido.cantidad_items() == 1
    assert pedido.precio() == dicc_precios_1["Salmón a la plancha"]

def test_quitar_item_a_pedido_actualiza_el_precio_total():
    pedido = Pedido(mesa_1, menu_1)
    pedido.agregar_item("Cafe con leche")
    pedido.agregar_item("Croissant nutella")
    pedido.quitar_item("Croissant nutella")
    assert pedido.precio() == dicc_precios_1["Cafe con leche"]

def item_entregado_no_puede_ser_borrado():
    pedido = Pedido(mesa_1, menu_1)
    pedido.agregar_item("Cafe con leche")
    pedido.agregar_item("Croissant nutella")
    pedido.entregar_item("Cafe con leche")
    assert not pedido.quitar_item("Cafe con leche")
    assert pedido.precio() == dicc_precios_1["Cafe con leche"]+dicc_precios_1["Croissant nutella"]

def agregar_descuento():
    pedido = Pedido(mesa_1, menu_1)
    pedido.agregar_item("Pizza margarita")
    pedido.agregar_descuento(4000)
    assert pedido.precio() == dicc_precios_1["Pizza margarita"]-4000

def test_pedido_cambia_de_mesa():
    pedido = Pedido(mesa_1)
    pedido.cambiar_mesa(mesa_2)
    assert pedido.mesa_actual() == mesa_2