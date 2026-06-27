from models.estanteria import Estanteria
from models.objeto import Objeto
from models.tipo_entidad import TipoEntidad


def test_contenedor_empieza_vacio():
    estanteria = Estanteria()

    assert estanteria.cantidad_objetos() == 0
    assert estanteria.objetos() == []


def test_agregar_objeto():
    estanteria = Estanteria()
    objeto = Objeto("Servilletero")

    estanteria.agregar_objeto(objeto)

    assert estanteria.cantidad_objetos() == 1
    assert estanteria.contiene(objeto)


def test_quitar_objeto():
    objeto = Objeto("Servilletero")
    estanteria = Estanteria([objeto])

    quitado = estanteria.quitar_objeto(objeto)

    assert quitado is objeto
    assert not estanteria.contiene(objeto)
    assert estanteria.cantidad_objetos() == 0


def test_quitar_objeto_inexistente():
    objeto = Objeto("Servilletero")
    estanteria = Estanteria()

    assert estanteria.quitar_objeto(objeto) is None


def test_objetos_devuelve_una_copia():
    objeto = Objeto("Servilletero")
    estanteria = Estanteria([objeto])

    copia = estanteria.objetos()
    copia.clear()

    assert estanteria.cantidad_objetos() == 1
    
def test_agregar_objeto_dentro_de_la_capacidad():
    estanteria = Estanteria(carga_max=10)

    servilletero = Objeto("Servilletero", peso=4)

    assert estanteria.agregar_objeto(servilletero)
    assert estanteria.cantidad_objetos() == 1
    
def test_no_agrega_objeto_si_excede_la_capacidad():
    estanteria = Estanteria(carga_max=5)

    servilletero = Objeto("Servilletero", peso=6)

    assert not estanteria.agregar_objeto(servilletero)
    assert estanteria.cantidad_objetos() == 0

def test_quitar_objeto_libera_capacidad():
    estanteria = Estanteria(carga_max=10)
    
    a = Objeto("Caja", peso=4)
    b = Objeto("Caja", peso=6)

    estanteria.agregar_objeto(a)
    estanteria.quitar_objeto(a)

    assert estanteria.agregar_objeto(b)