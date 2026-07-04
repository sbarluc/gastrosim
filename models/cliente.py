from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.pedido import Pedido

class Cliente(Entidad):
    
    def __init__(self, nombre, edad, specs=None):
        super().__init__(TipoEntidad.CLIENTE)

        self.nombre = nombre
        self.edad = edad
        
        self._specs = specs if specs is not None else []
        self._mesa_actual = None
        self._mesa_asignada = None
        self._sentado = False
        
        self._pedido = Pedido(cliente=self)

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
        return self._pedido.cantidad_items()
    
    def agregar_item(self, item):
        return self._pedido.agregar_item(item)
    
    def quitar_item(self, item):
        return self._pedido.quitar_item(item)
    
    def limpiar_items(self):
        self._pedido.limpiar_items()

    def items(self):
        return self._pedido.items()
    
    def valor_total_items(self):
        return self._pedido.valor()
    
    def preparar_item_para_pedir(self, item):
        item = self._pedido.buscar_item(item)
        if item:
            item.preparar_para_pedir()

    def __repr__(self):
        return self.nombre