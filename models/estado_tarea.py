from enum import Enum, auto

class EstadoTarea(Enum):
    PENDIENTE = auto()
    EN_PROGRESO = auto()
    COMPLETADA = auto()