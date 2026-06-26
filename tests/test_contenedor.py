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