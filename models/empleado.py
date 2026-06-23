from models.inventario import Inventario
from models.entidad import Entidad

class Empleado(Entidad):

    def __init__(self, nombre, puesto): 
        super().__init__()
        
        self.nombre = nombre
        self.puesto = puesto

        self._estado = "libre"
        self._posicion = None
        self._inventario = Inventario()

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

    def __repr__(self):
        return (
            f"      |{self.id_gral} - Empleado[{self.id}] - {self.nombre}, {self.puesto}\n"
            f"      |inventario: {self._inventario}\n"
        )