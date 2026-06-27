from models.contenedor import Contenedor
from models.objeto import Objeto
from models.tipo_entidad import TipoEntidad


def test_contenedor_empieza_vacio():
    contenedor = Contenedor(TipoEntidad.ESTANTERIA)

    assert contenedor.cantidad_objetos() == 0
    assert contenedor.objetos() == []


def test_agregar_objeto():
    contenedor = Contenedor(TipoEntidad.ESTANTERIA)
    objeto = Objeto("Servilletero")

    contenedor.agregar_objeto(objeto)

    assert contenedor.cantidad_objetos() == 1
    assert contenedor.contiene(objeto)


def test_quitar_objeto():
    objeto = Objeto("Servilletero")
    contenedor = Contenedor(TipoEntidad.ESTANTERIA, [objeto])

    quitado = contenedor.quitar_objeto(objeto)

    assert quitado is objeto
    assert not contenedor.contiene(objeto)
    assert contenedor.cantidad_objetos() == 0


def test_quitar_objeto_inexistente():
    objeto = Objeto("Servilletero")
    contenedor = Contenedor(TipoEntidad.ESTANTERIA)

    assert contenedor.quitar_objeto(objeto) is None


def test_objetos_devuelve_una_copia():
    objeto = Objeto("Servilletero")
    contenedor = Contenedor(TipoEntidad.ESTANTERIA, [objeto])

    copia = contenedor.objetos()
    copia.clear()

    assert contenedor.cantidad_objetos() == 1

def test_agregar_objeto():
    contenedor = Contenedor(TipoEntidad.ESTANTERIA)
    objeto = Objeto("Servilletero")

    contenedor.agregar_objeto(objeto)

    assert contenedor.cantidad_objetos() == 1
    assert contenedor.contiene(objeto)
    
def test_agregar_objeto_dentro_de_la_capacidad():
    contenedor = Contenedor(
        tipo=TipoEntidad.ESTANTERIA,
        carga_max=10
    )

    servilletero = Objeto("Servilletero", peso=4)

    assert contenedor.agregar_objeto(servilletero)
    assert contenedor.cantidad_objetos() == 1
    
def test_no_agrega_objeto_si_excede_la_capacidad():
    contenedor = Contenedor(
        tipo=TipoEntidad.INVENTARIO,
        carga_max=5
    )

    servilletero = Objeto("Servilletero", peso=6)

    assert not contenedor.agregar_objeto(servilletero)
    assert contenedor.cantidad_objetos() == 0
