import pytest
from models.estanteria import Estanteria
from models.objeto import Objeto
from models.tipo_entidad import TipoEntidad

@pytest.fixture
def servilletero():
    return Objeto("Servilletero")
@pytest.fixture
def estanteria_1():
    return Estanteria()
@pytest.fixture
def estanteria_2(servilletero):
    return Estanteria([servilletero])
@pytest.fixture
def estanteria_5():
    return Estanteria(carga_max=5)
@pytest.fixture
def estanteria_10():
    return Estanteria(carga_max=10)
@pytest.fixture
def caja_4():
    return Objeto("Caja", peso=4)
@pytest.fixture
def caja_6():
    return Objeto("Caja", peso=6)

def test_contenedor_empieza_vacio(estanteria_1):
    assert estanteria_1.cantidad_objetos() == 0
    assert estanteria_1.objetos() == []

def test_agregar_objeto(estanteria_1, servilletero):
    estanteria_1.agregar_objeto(servilletero)

    assert estanteria_1.cantidad_objetos() == 1
    assert estanteria_1.contiene(servilletero)

def test_quitar_objeto(estanteria_2, servilletero):
    quitado = estanteria_2.quitar_objeto(servilletero)

    assert quitado is servilletero
    assert not estanteria_2.contiene(servilletero)
    assert estanteria_2.cantidad_objetos() == 0

def test_quitar_objeto_inexistente(estanteria_1, servilletero):
    assert estanteria_1.quitar_objeto(servilletero) is None

def test_objetos_devuelve_una_copia(estanteria_2):
    copia = estanteria_2.objetos()
    copia.clear()

    assert estanteria_2.cantidad_objetos() == 1
    
def test_agregar_objeto_dentro_de_la_capacidad(estanteria_10, caja_4):
    assert estanteria_10.agregar_objeto(caja_4)
    assert estanteria_10.cantidad_objetos() == 1
    
def test_no_agrega_objeto_si_excede_la_capacidad(estanteria_5, caja_6):
    assert not estanteria_5.agregar_objeto(caja_6)
    assert estanteria_5.cantidad_objetos() == 0

def test_quitar_objeto_libera_capacidad(estanteria_10, caja_4, caja_6):
    estanteria_10.agregar_objeto(caja_4)
    estanteria_10.quitar_objeto(caja_4)

    assert estanteria_10.agregar_objeto(caja_6)