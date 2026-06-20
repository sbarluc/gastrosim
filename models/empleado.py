from models.entidad import Entidad
from models.inventario import Inventario
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
        
        self.inventario.agregar_objeto(objeto)
        origen.quitar_objeto(objeto)

    def dejar_objeto(self, destino, objeto):
        if not self.inventario.contiene(objeto):
            return False

        self.inventario.quitar_objeto(objeto)
        destino.agregar_objeto(objeto)

        return True

    def asignar_mesa_a_cliente(self, cliente, mesa):
        cliente.asignar_mesa(mesa)

    def __repr__(self):
        return (
            f"      |Empleado[{self.id}] - {self.nombre}, {self.puesto}\n"
            f"      |inventario: {self.inventario}\n"
        )