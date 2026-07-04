from models.inventario import Inventario
from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.pedido import Pedido

class Empleado(Entidad):

    def __init__(self, nombre, puesto): 
        super().__init__(TipoEntidad.EMPLEADO)
        
        self.nombre = nombre
        self.puesto = puesto

        self._estado = "libre"
        self._posicion = None
        self._inventario = Inventario()
        self._pedidos = {}

    def cargar_objeto(self, origen, objeto):
        if self._inventario.contiene(objeto):
            return False
        
        objeto = origen.quitar_objeto(objeto)
        if objeto is None:
            return False
        
        self._inventario.agregar_objeto(objeto)
        return True

    def dejar_objeto(self, destino, objeto):
        if not self._inventario.contiene(objeto):
            return False

        objeto = self._inventario.quitar_objeto(objeto)
        if objeto is None:
            return False
        
        destino.agregar_objeto(objeto)
        return True

    def asignar_mesa_a_cliente(self, cliente, mesa):
        cliente.asignar_mesa(mesa)

    def inventario(self):
        return self._inventario

    def crear_pedido(self, mesa):
        if mesa and not mesa.id in self._pedidos:
            pedido = Pedido(mesa)
            if pedido:
                self._pedidos[mesa.id] = Pedido(mesa)
                return True
        return False

    def agregar_item_a_pedido(self, mesa, item):
        if mesa.id in self._pedidos:
            return self._pedidos[mesa.id].agregar_item(item)
        return False

    def tomar_pedido_a_mesa(self, mesa):
        pedido_mesa = self.pedido_de_mesa(mesa)
        if pedido_mesa is None:
            return False
        
        for cliente in mesa.clientes_sentados():
            for item in cliente.items():
                if item.esta_para_pedir():
                    if pedido_mesa.agregar_item(item):
                        item.pedir()
        
        return True

    def cerrar_pedido(self, mesa):
        if mesa.id in self._pedidos:
            del self._pedidos[mesa.id]
            return True
        return False

    def pedido_de_mesa(self, mesa):
        if mesa.id in self._pedidos:
            return self._pedidos[mesa.id]
        return None

    def cantidad_pedidos(self):
        return len(self._pedidos)
    
    def pedidos(self):
        return self._pedidos.copy()

    def total_pedidos(self):
        return sum([pedido.valor() for id, pedido in self._pedidos.items()])

    def resumen_pedido(self, mesa):
        if mesa.id in self._pedidos:
            return {
                "mesa": mesa,
                "items": self._pedidos[mesa.id].items(),
                "total": self._pedidos[mesa.id].valor()
            }
        return None

    def entregar_item_de_pedido(self, mesa, item):
        if mesa.id in self._pedidos:
            item = self._pedidos[mesa.id].buscar_item(item)
            if item:
                item.entregar()

    def __repr__(self):
        return self.nombre