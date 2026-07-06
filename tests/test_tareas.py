import pytest # pyright: ignore[reportMissingImports]
from models.tarea import Tarea

# @pytest.fixture
# def tarea_nueva():
#     return 

# Tarea
# - id
# - tipo
# - objetivo
# - duracion_total
# - duracion_restante
# - estado
# + avanzar()
# + iniciar()
# + cancelar()
# + completar()

# Tests
def test_crear_tarea():
    tarea = Tarea("Limpiar mesa", 3)
    assert tarea.tipo == "Limpiar mesa"
    assert tarea.duracion_total == 3
    assert tarea.duracion_restante == 3

def test_tarea_empieza_pendiente():
    tarea = Tarea("Limpiar mesa", 3)
    assert tarea.esta_pendiente()