import pytest # pyright: ignore[reportMissingImports]
from models.tarea import Tarea

@pytest.fixture
def tarea_nueva():
    return Tarea("Limpiar mesa", 3)

# Tests
def test_crear_tarea():
    tarea = Tarea("Limpiar mesa", 3)
    assert tarea.tipo == "Limpiar mesa"
    assert tarea.duracion_total == 3
    assert tarea.duracion_restante == 3

def test_tarea_empieza_pendiente(tarea_nueva):
    assert tarea_nueva.esta_pendiente()

def test_tarea_empieza_no_completada(tarea_nueva):
    assert not tarea_nueva.esta_completada()

def test_iniciar_tarea(tarea_nueva):
    tarea_nueva.iniciar()
    assert tarea_nueva.esta_en_progreso()

def test_tarea_pendiente_no_puede_avanzar(tarea_nueva):
    tarea_nueva.avanzar()
    assert tarea_nueva.duracion_restante == 3

def test_tarea_iniciada_avanza_y_consume_tiempo(tarea_nueva):
    tarea_nueva.iniciar()
    tarea_nueva.avanzar()
    assert tarea_nueva.duracion_restante == 2

def test_tarea_termina_automaticamente(tarea_nueva):
    tarea_nueva.iniciar()
    tarea_nueva.avanzar()
    tarea_nueva.avanzar()
    tarea_nueva.avanzar()
    assert tarea_nueva.esta_completada()

def test_tarea_no_completada_no_puede_avanzar(tarea_nueva):
    tarea_nueva.iniciar()
    tarea_nueva.avanzar()
    tarea_nueva.avanzar()
    tarea_nueva.avanzar()
    tarea_nueva.avanzar()
    assert tarea_nueva.duracion_restante == 0

def test_cancelar_tarea(tarea_nueva):
    tarea_nueva.cancelar()
    assert tarea_nueva.esta_cancelada()

def test_tarea_cancelada_no_puede_avanzar(tarea_nueva):
    tarea_nueva.iniciar()
    tarea_nueva.cancelar()
    tarea_nueva.avanzar()
    assert tarea_nueva.duracion_restante == 3
