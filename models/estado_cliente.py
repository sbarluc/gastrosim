from enum import Enum, auto

class EstadoCliente(Enum):
    ASIGNADO_A_MESA = auto()
    SENTADO = auto()
    IMPACIENTE = auto()
    COMIENDO = auto()
    ESPERANDO_MESA = auto()
    RECLAMANDO_MESA = auto()
    ENOJADO = auto()
    HAMBRIENTO = auto()