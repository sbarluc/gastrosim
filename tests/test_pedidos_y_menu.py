import pytest # type: ignore
from models.mesa import Mesa
from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido
from models.pedido import Pedido

@pytest.fixture
def menu():
    return Menu(dicc_precios)
@pytest.fixture
def mesa():
    return Mesa(2)
@pytest.fixture
def pedido(mesa):
    return Pedido(mesa)

# ---------------------------------------------------------------------------------

def test_menu_se_crea_con_diccionario(menu):
    assert menu.precio("Cafe con leche") == 3000
    assert menu.precio("Croissant nutella") == 4000
    assert menu.precio("Salmón a la plancha") == 9800
    assert menu.precio("Pizza margarita") == 7500


def test_menu_precio_inexistente(menu):
    assert menu.precio("Plato inexistente") is None
    assert menu.precio("") is None

# ---------------------------------------------------------------------------------

def test_item_pedido_se_crea_sin_menu():
    item = ItemPedido("Salsa extra", 1500)
    assert item.nombre == "Salsa extra"
    assert item.valor() == 1500
    item2 = ItemPedido("Descuento", -10000)
    assert item2.nombre == "Descuento"
    assert item2.valor() == -10000

def test_item_pedido_se_crea_desde_menu(menu):
    item = ItemPedido.desde_menu(menu, "Cafe con leche")
    assert item.nombre == "Cafe con leche"
    assert item.valor() == 3000
    item2 = ItemPedido.desde_menu(menu, "Lomo saltado")
    assert item2.nombre == "Lomo saltado"
    assert item2.valor() == 9200

def test_item_pedido_con_nombre_inexistente(menu):
    item = ItemPedido.desde_menu(menu, "Plato inexistente")
    assert item is None

def test_item_pedido_entregar(menu):
    item = ItemPedido("Salero")
    assert item.fue_entregado() is False
    item.entregar()
    assert item.fue_entregado() is True

# ---------------------------------------------------------------------------------

def test_agregar_item_a_pedido(pedido, menu):
    assert pedido.cantidad_items() == 0
    assert pedido.agregar_item(ItemPedido.desde_menu(menu, "Cafe con leche"))
    assert pedido.cantidad_items() == 1
    assert pedido.valor() == 3000


def test_agregar_multiple_items(pedido, menu):
    assert pedido.agregar_item(ItemPedido.desde_menu(menu, "Cafe con leche"))
    assert pedido.agregar_item(ItemPedido("Salsa extra", 1500))
    assert pedido.agregar_item(ItemPedido.desde_menu(menu, "Salmón a la plancha"))
    
    assert pedido.cantidad_items() == 3
    assert pedido.valor() == 3000 + 1500 + 9800


def test_agregar_item_inexistente(pedido, menu):
    assert not pedido.agregar_item(ItemPedido.desde_menu(menu, "Tecito de ayahuasca"))
    assert pedido.cantidad_items() == 0
    assert pedido.valor() == 0


def test_agregar_item_duplicado(pedido, menu):
    assert pedido.agregar_item(ItemPedido.desde_menu(menu, "Cafe con leche"))
    assert pedido.agregar_item(ItemPedido.desde_menu(menu, "Cafe con leche"))
    
    assert pedido.cantidad_items() == 2
    assert pedido.valor() == 6000  # 3000 * 2


