from enum import Enum, auto

class TipoEntidad(Enum):
    CLIENTE = auto()
    EMPLEADO = auto()

    INVENTARIO = auto()
    MESA = auto()
    SILLA = auto()
    ESTANTERIA = auto()

    OBJETO = auto()