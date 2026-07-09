import pytest # pyright: ignore[reportMissingImports]
from models.empleado import Empleado
from models.mesa import Mesa

@pytest.fixture
def empleado_1():
    return Empleado("Seve", "Mozo")

@pytest.fixture
def mesa_1():
    return Mesa(1)

# Tests
def test_crear_empleado(empleado_1):
    assert empleado_1 is not None

def test_empleado_empieza_con_inventario_vacio(empleado_1):
    assert empleado_1.inventario().cantidad_objetos() == 0
    
def test_empleado_empieza_sin_pedidos(empleado_1):
    assert empleado_1.cantidad_pedidos() == 0
    assert empleado_1.pedidos() == {}

def test_empleado_crear_pedido_para_mesa(empleado_1, mesa_1):
    assert empleado_1.crear_pedido(mesa_1)
    assert empleado_1.cantidad_pedidos() == 1
    assert mesa_1.id in empleado_1.pedidos()
    assert empleado_1.valor_total_pedidos() == 0
    pedido = empleado_1.pedido_de_mesa(mesa_1)
    assert pedido is not None
    assert pedido.valor() == 0
    assert pedido.mesa_actual() == mesa_1

def test_empleado_no_crear_pedido_duplicado(empleado_1, mesa_1):
    empleado_1.crear_pedido(mesa_1)
    assert not empleado_1.crear_pedido(mesa_1)
    assert empleado_1.cantidad_pedidos() == 1