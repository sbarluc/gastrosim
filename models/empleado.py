class Empleado:

    def __init__(self, nombre, puesto):

        self.nombre = nombre
        self.puesto = puesto

        self.estado = "libre"
        self.posicion = None

        self.inventario = []

    def cargar_objeto(self, objeto):
        self.inventario.append(objeto)

    def dejar_objeto(self, mesa, objeto):
        if objeto not in self.inventario:
            return False

        self.inventario.remove(objeto)
        mesa.agregar_objeto(objeto)

        return True

    def __repr__(self):
        return (
            f"Empleado("
            f"nombre='{self.nombre}', "
            f"puesto='{self.puesto}', "
            f"objetos={len(self.inventario)}"
            f")"
        )