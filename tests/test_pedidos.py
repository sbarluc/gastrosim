import pytest
from models.mesa import Mesa
from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido
from models.pedido import Pedido

# Fixtures para datos básicos
@pytest.fixture
def dicc_precios_1():
    return dicc_precios()

@pytest.fixture
def menu_1(dicc_precios_1):
    return Menu(dicc_precios_1)

@pytest.fixture
def mesa_1():
    return Mesa(1)

@pytest.fixture
def mesa_2():
    return Mesa(1)

@pytest.fixture
def pedido_vacio(mesa_1):
    return Pedido(mesa_1)

@pytest.fixture
def pedido_con_menu(mesa_1, menu_1):
    return Pedido(mesa_1, menu_1)

@pytest.fixture
def pedido_con_items(pedido_con_menu):
    pedido_con_menu.agregar_item("Cafe con leche")
    pedido_con_menu.agregar_item("Croissant nutella")
    return pedido_con_menu

# Tests
def test_menu_recibe_diccionario_de_precios(menu_1, dicc_precios_1):
    assert menu_1.precio("Croissant nutella") == dicc_precios_1["Croissant nutella"]
    
def test_crear_item_desde_un_menu(menu_1, dicc_precios_1):
    item_pedido = ItemPedido(menu_1, "Croissant nutella")
    assert item_pedido.valor() == dicc_precios_1["Croissant nutella"]

def test_pedido_para_mesa_comienza_vacio(pedido_vacio, mesa_1):
    assert pedido_vacio.cantidad_items() == 0
    assert pedido_vacio.valor() == 0
    assert pedido_vacio.mesa_actual() == mesa_1

def test_agregar_item_a_pedido_actualiza_el_precio_total(pedido_con_menu, dicc_precios_1):
    pedido_con_menu.agregar_item("Salmón a la plancha")
    assert pedido_con_menu.cantidad_items() == 1
    assert pedido_con_menu.valor() == dicc_precios_1["Salmón a la plancha"]

def test_quitar_item_a_pedido_actualiza_el_precio_total(pedido_con_menu, dicc_precios_1):
    pedido_con_menu.agregar_item("Cafe con leche")
    pedido_con_menu.agregar_item("Croissant nutella")
    pedido_con_menu.quitar_item("Croissant nutella")
    assert pedido_con_menu.valor() == dicc_precios_1["Cafe con leche"]

def test_item_entregado_no_puede_ser_borrado(pedido_con_menu, dicc_precios_1):
    pedido_con_menu.agregar_item("Cafe con leche")
    pedido_con_menu.agregar_item("Croissant nutella")
    pedido_con_menu.entregar_item("Cafe con leche")
    assert not pedido_con_menu.quitar_item("Cafe con leche")
    assert pedido_con_menu.valor() == dicc_precios_1["Cafe con leche"] + dicc_precios_1["Croissant nutella"]

def test_agregar_descuento(pedido_con_menu, dicc_precios_1):
    pedido_con_menu.agregar_item("Pizza margarita")
    pedido_con_menu.agregar_descuento(4000)
    assert pedido_con_menu.valor() == dicc_precios_1["Pizza margarita"] - 4000

def test_pedido_cambia_de_mesa(mesa_1, mesa_2):
    pedido = Pedido(mesa_1)
    pedido.cambiar_mesa(mesa_2)
    assert pedido.mesa_actual() == mesa_2

def test_pedido_puede_tener_multiples_items(pedido_con_menu, dicc_precios_1):
    items = ["Cafe con leche", "Croissant nutella", "Salmón a la plancha"]
    precio_esperado = 0
    
    for item in items:
        pedido_con_menu.agregar_item(item)
        precio_esperado += dicc_precios_1[item]
    
    assert pedido_con_menu.cantidad_items() == 3
    assert pedido_con_menu.valor() == precio_esperado

def test_quitar_item_inexistente_no_cambia_el_pedido(pedido_con_menu):
    pedido_con_menu.agregar_item("Cafe con leche")
    precio_original = pedido_con_menu.valor()
    
    resultado = pedido_con_menu.quitar_item("Item inexistente")
    
    assert not resultado
    assert pedido_con_menu.cantidad_items() == 1
    assert pedido_con_menu.valor() == precio_original