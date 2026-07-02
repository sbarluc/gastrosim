from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad

class Cliente(Entidad):
    
    def __init__(self, nombre, edad, specs=None):
        super().__init__(TipoEntidad.CLIENTE)

        self.nombre = nombre
        self.edad = edad
        
        self._specs = specs if specs is not None else []
        self._mesa_actual = None
        self._mesa_asignada = None
        self._sentado = False
        self._items = []
        self._valor_total_items = 0

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
        if self._mesa_actual is None:
            return False

        self._mesa_actual.desocupar_silla(self)
        self._mesa_actual = None
        self._sentado = False
        return True

    def mesa_actual(self):
        return self._mesa_actual
    
    def mesa_asignada(self):
        return self._mesa_asignada

    def cantidad_items(self):
        return len(self._items)
    
    def agregar_item(self, item):
        if item is None or item in self._items:
            return False
        self._items.append(item)
        self._valor_total_items += item.valor()
        return True
    
    def quitar_item(self, item):
        if item is None or item in self._items:
            return False
        self._items.append(item)
        self._valor_total_items += item.valor()
        return True

    def items(self):
        return self._items.copy()
    
    def valor_total_items(self):
        return self._valor_total_items

    def __repr__(self):
        return self.nombre