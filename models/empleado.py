from models.inventario import Inventario
from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.pedido import Pedido
from models.posicion import Posicion

class Empleado(Entidad):

    def __init__(self, nombre, puesto, x=0, y=0): 
        super().__init__(TipoEntidad.EMPLEADO, nombre=nombre)
        
        self.nombre = nombre
        self.puesto = puesto

        self._inventario = Inventario()
        self._pedidos = {}

        self.posicion = Posicion()
    

    def cargar_objeto_desde(self, objeto, origen):
        _objeto = origen.quitar_objeto(objeto)
        if _objeto is None:
            return False
        self._inventario.agregar_objeto(_objeto)
        return True

    def dejar_objeto_en(self, objeto, destino):
        _objeto = self._inventario.quitar_objeto(objeto)
        if _objeto is None:
            return False
        destino.agregar_objeto(_objeto)
        return True

    def inventario(self):
        return self._inventario
    
    def crear_pedido(self, mesa):
        if mesa and not mesa.id in self._pedidos:
            pedido = Pedido(mesa)
            if pedido:
                self._pedidos[mesa.id] = Pedido(mesa)
                return True
        return False
    
    def cantidad_pedidos(self):
        return len(self._pedidos)
    
    def pedidos(self):
        return self._pedidos.copy()

    def pedido_de_mesa(self, mesa):
        if mesa.id in self._pedidos:
            return self._pedidos[mesa.id]
        return None

    def valor_total_pedidos(self):
        return sum([pedido.valor() for id, pedido in self._pedidos.items()])

    def resumen_pedido(self, mesa):
        if mesa.id in self._pedidos:
            return {
                "mesa": mesa,
                "items": self._pedidos[mesa.id].items(),
                "total": self._pedidos[mesa.id].valor()
            }
        return None

    def info(self):
        pedidos = ""
        for id in self._pedidos:
            pedidos += (f"\nPedido[Mesa{id}]:\n{self._pedidos[id].info()}" if self._pedidos[id].cantidad_items()>0 else "")
        return (
            f"[{self.id}] {self.nombre}, {self.puesto}\n" + \
            f"Inventario: {self._inventario.info()}" + \
            pedidos
        )
    
    
    

    # ### OUTDATED

    # ### OUTDATED
    # def asignar_mesa_a_cliente(self, cliente, mesa):
    #     cliente.asignar_mesa(mesa)
    # ### OUTDATED
    # def desasignar_mesa_a_cliente(self, cliente, mesa):
    #     cliente.desasignar_mesa(mesa)
    # ### OUTDATED

    # ### OUTDATED
    # def agregar_item_a_pedido(self, mesa, item):
    #     if mesa.id in self._pedidos:
    #         return self._pedidos[mesa.id].agregar_item(item)
    #     return False
    # ### OUTDATED
    # def quitar_item_a_pedido(self, mesa, item):
    #     if mesa.id in self._pedidos:
    #         return self._pedidos[mesa.id].quitar_item(item)
    #     return False
    # ### OUTDATED
    # def limpiar_items_de_pedido(self, mesa):
    #     if mesa.id in self._pedidos:
    #         return self._pedidos[mesa.id].limpiar_items()
    #     return False
    # ### OUTDATED
    # def tomar_pedido_a_mesa(self, mesa):
    #     pedido_mesa = self.pedido_de_mesa(mesa)
    #     if pedido_mesa is None:
    #         return False
        
    #     for cliente in mesa.clientes_sentados():
    #         for item in cliente.items():
    #             if item.esta_para_pedir():
    #                 if pedido_mesa.agregar_item(item):
    #                     item.pedir()
        
    #     return True
    # ### OUTDATED
    # def cerrar_pedido(self, mesa):
    #     if mesa.id in self._pedidos:
    #         del self._pedidos[mesa.id]
    #         return True
    #     return False
    # ### OUTDATED
    # def entregar_item_de_pedido(self, mesa, item):
    #     if mesa.id in self._pedidos:
    #         item = self._pedidos[mesa.id].buscar_item(item)
    #         if item:
    #             item.entregar()
    # ### OUTDATED