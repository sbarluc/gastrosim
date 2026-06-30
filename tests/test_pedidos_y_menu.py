import pytest # type: ignore
from models.mesa import Mesa
from models.menu import Menu
from data.test_menu import dicc_precios
from models.item_pedido import ItemPedido
from models.pedido import Pedido

@pytest.fixture
def menu():
    """Menu creado a partir del diccionario de precios de prueba."""
    return Menu(dicc_precios())
@pytest.fixture
def mesa():
    """Mesa con capacidad para 2 personas."""
    return Mesa(2)
@pytest.fixture
def pedido(mesa):
    return Pedido(mesa)

def test_menu_se_crea_con_diccionario(menu):
    assert menu.precio("Cafe con leche") == 3000
    assert menu.precio("Croissant nutella") == 4000
    assert menu.precio("Salmón a la plancha") == 9800
    assert menu.precio("Pizza margarita") == 7500


def test_menu_precio_inexistente(menu):
    assert menu.precio("Plato inexistente") is None
    assert menu.precio("") is None



def test_item_pedido_se_crea_desde_menu(menu):
    item = ItemPedido(menu, "Cafe con leche")
    assert item.nombre == "Cafe con leche"
    assert item.valor() == 3000

    item2 = ItemPedido(menu, "Croissant nutella")
    assert item2.nombre == "Croissant nutella"
    assert item2.valor() == 4000

def test_item_pedido_con_nombre_inexistente(menu):
    item = ItemPedido(menu, "Plato inexistente")
    assert item.nombre == "Plato inexistente"
    assert item.valor() == None

def test_item_pedido_sin_menu():
    item = ItemPedido()
    assert item.nombre == ""
    assert item.valor() == 0


def test_item_pedido_entregar(menu):
    item = ItemPedido(menu, "Cafe con leche")
    assert item.fue_entregado() is False
    item.entregar()
    assert item.fue_entregado() is True

def test_item_pedido_descuento(menu):
    item_descuento = ItemPedido().descuento(2000)
    assert item_descuento.nombre == "Descuento"
    assert item_descuento.valor() == 2000
