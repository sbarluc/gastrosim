from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.pedido import Pedido
from models.estado_cliente import EstadoCliente
from models.item_pedido import ItemPedido
from models.posicion import Posicion

class Cliente(Entidad):
    
    def __init__(self, nombre, edad):
        super().__init__(TipoEntidad.CLIENTE, nombre=nombre)

        self.edad = edad
        self.mesa_actual = None
        self.estados = set([EstadoCliente.ESPERANDO_MESA])
        self.paciencia = 100
        self.hambre = 0
        self._mesa_asignada = None
        self._sentado = False
        self._pedido = Pedido(cliente=self)

        self.posicion = Posicion()

    # Consultas

    def tiene_estado(self, estado):
        return estado in self.estados

    def agregar_estado(self, estado):
        self.estados.add(estado)

    def quitar_estado(self, estado):
        self.estados.discard(estado)

    def limpiar_estados(self):
        self.estados = set()

    def lista_estados(self):
        return [e.name for e in self.estados]

    def esta_sentado(self):
        return self.tiene_estado(EstadoCliente.SENTADO)

    # Mesa

    def asignar_mesa(self, mesa):
        self._mesa_asignada = mesa
        self.estados.add(EstadoCliente.ASIGNADO_A_MESA)
        self.estados.discard(EstadoCliente.ESPERANDO_MESA)

    def desasignar_mesa(self):
        self._mesa_asignada = None
        self.estados.discard(EstadoCliente.ASIGNADO_A_MESA)

    def sentarse_en_mesa(self, mesa):
        if (not mesa.tiene_lugar() or self.tiene_estado(EstadoCliente.SENTADO)):
            return False
        
        mesa.ocupar_silla(self)
        self.estados.add(EstadoCliente.SENTADO)
        self.mesa_actual = mesa
        return True

    def pararse(self):
        if self.mesa_actual is None:
            return False

        self.mesa_actual.desocupar_silla(self)
        self.mesa_actual = None
        self.estados.discard(EstadoCliente.SENTADO)

        return True
    
    def mesa_asignada(self):
        return self._mesa_asignada

    def pedido(self):
        return self._pedido
    
    def tomar_pedido(self):
        return self._pedido.items_para_pedir()

    def lista_estados(self):
        return [e.name for e in self.estados]
    
    def tick(self, sim):
        self.actualizar_necesidades()
        self.actualizar_estados()
        self.decidir(sim)

    def actualizar_necesidades(self):
        if self.tiene_estado(EstadoCliente.MUERTO):
            return

        if self.tiene_estado(EstadoCliente.COMIENDO):
            self.hambre = max(0, self.hambre - 1)
        else:
            self.hambre += 0.1
            
        self.paciencia = min(100, self.paciencia + 0.1)
        if self.tiene_estado(EstadoCliente.ESPERANDO_MESA):
            self.paciencia -= 1

    def actualizar_estados(self):
        if self.paciencia <= 20 and self.tiene_estado(EstadoCliente.ESPERANDO_MESA):
            self.agregar_estado(EstadoCliente.IMPACIENTE)
        else:
            self.quitar_estado(EstadoCliente.IMPACIENTE)

        if self.paciencia <= 0:
            self.agregar_estado(EstadoCliente.RECLAMANDO_MESA)
            self.agregar_estado(EstadoCliente.ENOJADO)
        else:
            self.quitar_estado(EstadoCliente.RECLAMANDO_MESA)
            self.quitar_estado(EstadoCliente.ENOJADO)

        if self.hambre > 200:
            self.limpiar_estados()
            self.agregar_estado(EstadoCliente.MUERTO)

    def decidir(self, sim):
        if self.tiene_estado(EstadoCliente.MUERTO):
            return 
        if self.tiene_estado(EstadoCliente.ESPERANDO_MESA) and self.tiene_estado(EstadoCliente.IMPACIENTE):
            mesa_libre = sim.buscar_mesa_libre()
            if mesa_libre:
                self.sentarse_en_mesa(mesa_libre)

        if self.tiene_estado(EstadoCliente.ASIGNADO_A_MESA):
            self.sentarse_en_mesa(self._mesa_asignada)

        if self.tiene_estado(EstadoCliente.SENTADO) and self._pedido.cantidad_items() == 0 and self.mesa_actual.obtener_objeto("Menu") is None:
            self._pedido.agregar_item(ItemPedido("Menu"))

    # Debug

    def info(self):
        return (
            f"[{self.id}] {self.nombre}, {self.edad} años\n"
            f"* Mesa actual: {self.mesa_actual.id if self.mesa_actual else '-'}"
            f" | Mesa asignada: {self._mesa_asignada.id if self._mesa_asignada else '-'}\n"
            f"* Estados: {self.lista_estados()}\n"
            f"* Paciencia: {self.paciencia:.1f}"
            f" | Hambre: {self.hambre:.1f}"
            + (
                f"\n* Pedido:\n{self._pedido.info()}"
                if self._pedido.cantidad_items() > 0
                else ""
            )
        )