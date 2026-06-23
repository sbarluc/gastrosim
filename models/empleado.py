from models.inventario import Inventario
from models.entidad import Entidad

class Empleado(Entidad):

    def __init__(self, nombre, puesto): 
        super().__init__()
        
        self.nombre = nombre
        self.puesto = puesto
        self.estado = "libre"
        self.posicion = None
        self.inventario = Inventario()

    def cargar_objeto(self, origen, objeto):
        if self.inventario.contiene(objeto):
            return False
        
        objeto = origen.quitar_objeto(objeto)
        if objeto is None:
            return False
        
        self.inventario.agregar_objeto(objeto)
        return True

    def dejar_objeto(self, destino, objeto):
        if not self.inventario.contiene(objeto):
            return False

        objeto = self.inventario.quitar_objeto(objeto)
        if objeto is None:
            return False
        
        destino.agregar_objeto(objeto)
        return True

    def asignar_mesa_a_cliente(self, cliente, mesa):
        cliente.asignar_mesa(mesa)

    def __repr__(self):
        return (
            f"      |{self.id_gral} - Empleado[{self.id}] - {self.nombre}, {self.puesto}\n"
            f"      |inventario: {self.inventario}\n"
        )