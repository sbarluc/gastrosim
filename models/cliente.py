from models.entidad import Entidad
from models.tipo_entidad import TipoEntidad
from models.pedido import Pedido

class Cliente(Entidad):
    
    def __init__(self, nombre, edad, specs=None):
        super().__init__(TipoEntidad.CLIENTE, nombre=nombre)

        self.edad = edad
        self.mesa_actual = None
        self._mesa_asignada = None
        self._sentado = False
        self._pedido = Pedido(cliente=self)

    def esta_sentado(self):
        return self._sentado

    def asignar_mesa(self, mesa):
        self._mesa_asignada = mesa

    def desasignar_mesa(self):
        self._mesa_asignada = None

    def sentarse_en_mesa(self, mesa):
        if (not mesa.tiene_lugar() or self.esta_sentado()):
            return False
        
        mesa.ocupar_silla(self)
        self._sentado = True
        self.mesa_actual = mesa
        return True

    def pararse(self):
        if self.mesa_actual is None:
            return False

        self.mesa_actual.desocupar_silla(self)
        self.mesa_actual = None
        self._sentado = False

        return True
    
    def mesa_asignada(self):
        return self._mesa_asignada

    def pedido(self):
        return self._pedido
    
    def tomar_pedido(self):
        return self._pedido.items_para_pedir()

    def info(self):
        return (
            f"[{self.id}] {self.nombre}, {self.edad} años\n" + \
            f"Mesa actual: {self.mesa_actual.id if self.mesa_actual else '-'}" + \
            f" | Mesa asignada: {self._mesa_asignada.id if self._mesa_asignada else '-'}" + \
            (f" | Sentad@\n" if self.esta_sentado() else "") + \
            (f"Pedido: \n{self._pedido.info()}"  if self._pedido.cantidad_items() > 0 else "")
        )