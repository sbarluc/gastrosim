class Empleado:
    siguiente_id = 1

    def __init__(self, nombre, puesto):
        self.id = Empleado.siguiente_id
        Empleado.siguiente_id += 1
        
        self.nombre = nombre
        self.puesto = puesto

        self.estado = "libre"
        self.posicion = None

        self.inventario = []

    def cargar_objeto(self, origen, objeto):
        if objeto not in origen.objetos:
            return False
        
        self.inventario.append(objeto)
        origen.quitar_objeto(objeto)

    def dejar_objeto(self, destino, objeto):
        if objeto not in self.inventario:
            return False

        self.inventario.remove(objeto)
        destino.agregar_objeto(objeto)

        return True

    def asignar_cliente_a_mesa(self, cliente, mesa):
        mesa.asignar_cliente(cliente)

    def __repr__(self):
        return (
            f"      |Empleado[{self.id}] - {self.nombre}, {self.puesto}\n"
            f"      |objetos: {[o.nombre for o in self.inventario]}\n"
        )