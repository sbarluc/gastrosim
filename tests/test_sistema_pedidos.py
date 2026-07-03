import pytest # pyright: ignore[reportMissingImports]
from models.mesa import Mesa
from models.menu import Menu
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from models.cliente import Cliente
from models.empleado import Empleado
from data.test_menu import dicc_precios

@pytest.fixture
def menu():
    return Menu(dicc_precios)
@pytest.fixture
def mesa_1():
    return Mesa(2)
@pytest.fixture
def mesa_2():
    return Mesa(3)
@pytest.fixture
def empleado():
    return Empleado("Juan", "Mozo")
@pytest.fixture
def cliente_ana():
    return Cliente("Ana", 25)
@pytest.fixture
def cliente_carlos():
    return Cliente("Carlos", 30)
@pytest.fixture
def cliente_laura():
    return Cliente("Laura", 28)

#-------------------------------------------------------------------------------------

def test_cliente_empieza_sin_items(cliente_ana):
    assert cliente_ana.cantidad_items() == 0
    assert cliente_ana.items() == []

def test_cliente_agregar_item(cliente_ana):
    item = ItemPedido("Cenicero")
    assert cliente_ana.agregar_item(item)
    assert cliente_ana.cantidad_items() == 1
    assert cliente_ana.valor_total_items() == 0

def test_cliente_agregar_item_desde_menu(cliente_ana, menu):
    item = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    assert cliente_ana.agregar_item(item)
    assert cliente_ana.cantidad_items() == 1
    assert cliente_ana.valor_total_items() == 5000

def test_cliente_agregar_multiple_items(cliente_ana, menu):
    cenicero = ItemPedido("Cenicero")
    cafe_con_leche = ItemPedido.desde_menu(menu, "Cafe con leche")
    cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    assert cliente_ana.agregar_item(cheesecake)
    assert cliente_ana.agregar_item(cenicero)
    assert cliente_ana.agregar_item(cafe_con_leche)
    
    assert cliente_ana.cantidad_items() == 3
    assert cliente_ana.valor_total_items() == 8000

def test_cliente_agregar_item_inexistente(cliente_ana, menu):
    sanguche_de_miga = ItemPedido.desde_menu(menu, "Sanguche de miga")
    assert not cliente_ana.agregar_item(sanguche_de_miga)
    assert cliente_ana.cantidad_items() == 0
    assert cliente_ana.valor_total_items() == 0

def test_cliente_quitar_item(cliente_ana, menu):
    cafe_con_leche = ItemPedido.desde_menu(menu, "Cafe con leche")
    cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    cliente_ana.agregar_item(cafe_con_leche)
    cliente_ana.agregar_item(cheesecake)
    cliente_ana.quitar_item(cheesecake)
    assert cliente_ana.cantidad_items() == 1
    assert cliente_ana.valor_total_items() == 3000

#-----------------------------------------------------------------------

def test_cliente_preparar_item_para_pedir(cliente_ana):
    item = ItemPedido("Cenicero")
    cliente_ana.agregar_item(item)
    assert not cliente_ana.items()[0].esta_para_pedir()

    cliente_ana.preparar_item_para_pedir(item)
    assert cliente_ana.items()[0].esta_para_pedir()

#-----------------------------------------------------------------------

def test_empleado_tomar_pedido_a_mesa(empleado, cliente_ana, cliente_pedro, mesa1):
    empleado.asignar_mesa_a_cliente(cliente_ana, mesa1)
    empleado.asignar_mesa_a_cliente(cliente_pedro, mesa1)
    cliente_ana.sentarse_en(mesa1)
    cliente_pedro.sentarse_en(mesa1)
    
    cliente_ana.agregar_item(ItemPedido("servilletero"))
    cliente_pedro.agregar_item(ItemPedido("menu"))

    assert empleado.tomar_pedido(mesa1)
    assert empleado.pedido_para_mesa(mesa1).cantidad_items() == 2

