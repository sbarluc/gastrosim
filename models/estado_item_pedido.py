from enum import Enum, auto

class EstadoItemPedido(Enum):
    PARA_PEDIR = auto()
    ESPERANDO = auto()
    ENTREGADO = auto()