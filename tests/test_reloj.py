import pytest # pyright: ignore[reportMissingImports]
from models.reloj import Reloj

@pytest.fixture
def reloj_apertura():
    return Reloj(10,0)

# Tests
def test_reloj_con_parametros_fuera_de_rango_devuelve_medianoche():
    reloj = Reloj(-1,900)
    assert reloj.hora == 0
    assert reloj.minuto == 0

def test_crear_reloj(reloj_apertura):
    assert reloj_apertura.hora == 10
    assert reloj_apertura.minuto == 0

def test_avanzar_un_minuto(reloj_apertura):
    reloj_apertura.avanzar_minuto()
    assert reloj_apertura.hora == 10
    assert reloj_apertura.minuto == 1

def test_avanzar_varios_minutos(reloj_apertura):
    for _ in range(15):
        reloj_apertura.avanzar_minuto()

    assert reloj_apertura.hora == 10
    assert reloj_apertura.minuto == 15

def test_cambiar_de_hora(reloj_apertura):

    for _ in range(60):
        reloj_apertura.avanzar_minuto()

    assert reloj_apertura.hora == 11
    assert reloj_apertura.minuto == 0

def test_avanzar_dos_horas(reloj_apertura):

    for _ in range(120):
        reloj_apertura.avanzar_minuto()

    assert reloj_apertura.hora == 12
    assert reloj_apertura.minuto == 0

def test_avanzar_dos_horas(reloj_apertura):

    for _ in range(60*14):
        reloj_apertura.avanzar_minuto()

    assert reloj_apertura.hora == 0
    assert reloj_apertura.minuto == 0

def test_minutos_siempre_validos(reloj_apertura):
    for _ in range(2000):
        reloj_apertura.avanzar_minuto()

        assert 0 <= reloj_apertura.minuto < 60

def test_horas_siempre_validas(reloj_apertura):
    for _ in range(5000):
        reloj_apertura.avanzar_minuto()

        assert 0 <= reloj_apertura.hora < 24