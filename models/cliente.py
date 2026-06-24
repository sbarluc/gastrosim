from models.entidad import Entidad

class Cliente(Entidad):
    
    def __init__(self, nombre, edad, specs=None):
        super().__init__()

        self.nombre = nombre
        self.edad = edad
        
        self._specs = specs if specs is not None else []
        self._mesa_actual = None
        self._mesa_asignada = None
        self._sentado = False
    
    def asignar_mesa(self, mesa):
        self._mesa_asignada = mesa

    def agregar_spec(self, spec):
        self._specs.append(spec)

    def sentarse_en(self, mesa):
        if (not mesa.tiene_lugar() or self._sentado):
            return False
        
        mesa.ocupar_silla(self)
        self._sentado = True
        self._mesa_actual = mesa
        return True

    def pararse(self):
        self._mesa_actual.desocupar_silla(self)
        self._mesa_actual = None
        self._sentado = False

    def mesa_actual(self):
        return self._mesa_actual
    
    def mesa_asignada(self):
        return self._mesa_asignada

    def __repr__(self):
        return self.nombre