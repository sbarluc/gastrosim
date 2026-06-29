from models.estanteria import Estanteria
from models.objeto import Objeto
from models.tipo_entidad import TipoEntidad

servilletero = Objeto("Servilletero")
estanteria_10 = Estanteria(carga_max=10)
estanteria_5 = Estanteria(carga_max=5)
caja_4 = Objeto("Caja", peso=4)
caja_6 = Objeto("Caja", peso=6)

def test_contenedor_empieza_vacio():
    estanteria = Estanteria()

    assert estanteria.cantidad_objetos() == 0
    assert estanteria.objetos() == []


def test_agregar_objeto():
    estanteria = Estanteria()

    estanteria.agregar_objeto(servilletero)

    assert estanteria.cantidad_objetos() == 1
    assert estanteria.contiene(servilletero)


def test_quitar_objeto():
    estanteria = Estanteria([servilletero])

    quitado = estanteria.quitar_objeto(servilletero)

    assert quitado is servilletero
    assert not estanteria.contiene(servilletero)
    assert estanteria.cantidad_objetos() == 0


def test_quitar_objeto_inexistente():
    estanteria = Estanteria()

    assert estanteria.quitar_objeto(servilletero) is None


def test_objetos_devuelve_una_copia():
    estanteria = Estanteria([servilletero])

    copia = estanteria.objetos()
    copia.clear()

    assert estanteria.cantidad_objetos() == 1
    
def test_agregar_objeto_dentro_de_la_capacidad():
    assert estanteria_10.agregar_objeto(caja_4)
    assert estanteria_10.cantidad_objetos() == 1
    
def test_no_agrega_objeto_si_excede_la_capacidad():
    assert not estanteria_5.agregar_objeto(caja_6)
    assert estanteria_5.cantidad_objetos() == 0

def test_quitar_objeto_libera_capacidad():
    estanteria_10.agregar_objeto(caja_4)
    estanteria_10.quitar_objeto(caja_4)

    assert estanteria_10.agregar_objeto(caja_6)