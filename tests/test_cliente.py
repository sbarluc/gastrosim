import pytest # pyright: ignore[reportMissingImports]
from models.cliente import Cliente
from models.mesa import Mesa

@pytest.fixture
def cliente_1():
    return Cliente("Harry", 10)

@pytest.fixture
def mesa_1():
    return Mesa(1)

# Tests
def test_crear_cliente(cliente_1):
    assert cliente_1 is not None
    
def test_empleado_empieza_parado_y_sin_mesa(cliente_1):
    assert not cliente_1.esta_sentado()
    assert cliente_1.mesa_actual == None
    assert cliente_1.mesa_asignada() == None

def test_cliente_asignar_mesa(cliente_1, mesa_1):
    cliente_1.asignar_mesa(mesa_1)
    assert cliente_1.mesa_asignada() == mesa_1
    assert cliente_1.mesa_actual == None

def test_desasignar_mesa(cliente_1, mesa_1):
    cliente_1.asignar_mesa(mesa_1)
    cliente_1.desasignar_mesa()
    assert cliente_1.mesa_asignada() == None

def test_cliente_se_sienta_en_mesa(cliente_1, mesa_1):
    assert cliente_1.sentarse_en_mesa(mesa_1)
    assert cliente_1.mesa_actual == mesa_1
    assert cliente_1.mesa_asignada() == None
    assert cliente_1.esta_sentado()
    assert mesa_1.cantidad_sentados() == 1
    assert cliente_1 in mesa_1.clientes_sentados()

def test_cliente_se_para(cliente_1, mesa_1):
    assert cliente_1.sentarse_en_mesa(mesa_1)
    assert cliente_1.pararse()
    assert cliente_1.mesa_actual == None
    assert mesa_1.cantidad_sentados() == 0
    assert cliente_1 not in mesa_1.clientes_sentados()

def test_cliente_se_para_de_mesa_asignada(cliente_1, mesa_1):
    cliente_1.asignar_mesa(mesa_1)
    assert cliente_1.sentarse_en_mesa(mesa_1)
    assert cliente_1.pararse()
    assert cliente_1.mesa_asignada() == mesa_1

def test_cliente_no_puede_sentarse_en_mesa_llena(cliente_1, mesa_1):
    mesa_1.ocupar_silla(Cliente("Neville","10"))
    assert not cliente_1.sentarse_en_mesa(mesa_1)
    assert not cliente_1.esta_sentado()

def test_cliente_empieza_con_pedido_vacio(cliente_1):
    assert cliente_1.pedido().cantidad_items() == 0