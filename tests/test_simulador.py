import pytest # pyright: ignore[reportMissingImports]
from core.simulador import Simulador
from models.mesa import Mesa
from models.cliente import Cliente
from models.tarea import Tarea
from models.tipo_entidad import TipoEntidad


@pytest.fixture
def sim():
    return Simulador()
@pytest.fixture
def mesa_1():
    return Mesa(4)
@pytest.fixture
def mesa_2():
    return Mesa(2)
@pytest.fixture
def cliente_ana():
    return Cliente("Ana", 25)
@pytest.fixture
def tarea_1():
    return Tarea("Limpiar mesa", 3)


def test_crear_simulador():
    sim = Simulador()

    assert sim.reloj is not None
    assert sim.entidades == {}
    assert sim.tareas == []


def test_agregar_primera_entidad_crea_su_categoria(sim, mesa_1):
    sim.agregar_entidad(mesa_1)

    assert TipoEntidad.MESA in sim.entidades


def test_agregar_entidad(sim, mesa_1):
    sim.agregar_entidad(mesa_1)

    assert mesa_1 in sim.obtener_entidades(TipoEntidad.MESA)


def test_agregar_varias_mesas(sim, mesa_1, mesa_2):
    sim.agregar_entidad(mesa_1)
    sim.agregar_entidad(mesa_2)

    assert len(sim.obtener_entidades(TipoEntidad.MESA)) == 2


def test_agregar_distintos_tipos(sim, mesa_1, cliente_ana):
    sim.agregar_entidad(mesa_1)
    sim.agregar_entidad(cliente_ana)

    assert len(sim.obtener_entidades(TipoEntidad.MESA)) == 1
    assert len(sim.obtener_entidades(TipoEntidad.CLIENTE)) == 1


def test_obtener_categoria_vacia(sim):
    assert sim.obtener_entidades(TipoEntidad.EMPLEADO) == []


def test_quitar_entidad(sim, mesa_1):
    sim.agregar_entidad(mesa_1)
    sim.quitar_entidad(mesa_1)

    assert mesa_1 not in sim.obtener_entidades(TipoEntidad.MESA)


def test_agregar_tarea(sim, tarea_1):
    sim.agregar_tarea(tarea_1)

    assert tarea_1 in sim.tareas


def test_tick_avanza_reloj(sim):
    assert sim.reloj.hora == 0
    assert sim.reloj.minuto == 0
    assert sim.reloj.segundo == 0

    sim.tick()
    assert sim.reloj.hora == 0
    assert sim.reloj.minuto == 0
    assert sim.reloj.segundo == 1

    for _ in range(60):
        sim.tick()
        assert sim.reloj.hora == 0
        assert sim.reloj.minuto == 1
        assert sim.reloj.segundo == 1

    for _ in range(60*60):
        sim.tick()
        assert sim.reloj.hora == 1
        assert sim.reloj.minuto == 1
        assert sim.reloj.segundo == 1

    for _ in range(60*60*24):
        assert sim.reloj.hora == 1
        assert sim.reloj.minuto == 1
        assert sim.reloj.segundo == 1
        