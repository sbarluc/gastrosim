class Empleado:

    def __init__(self, nombre, puesto):

        self.nombre = nombre
        self.puesto = puesto

        self.estado = "libre"
        self.posicion = None

        self.inventario = []

    def cargar_objeto(self, origen, objeto):
        objeto_retirado = origen.quitar_objeto(objeto)
        if objeto_retirado is None:
            return False

        self.inventario.append(objeto_retirado)

        return True

    def dejar_objeto(self, destino, objeto):
        if objeto not in self.inventario:
            return False

        self.inventario.remove(objeto)
        destino.agregar_objeto(objeto)

        return True

    def __repr__(self):
        return (
            f"Empleado("
            f"nombre='{self.nombre}', "
            f"puesto='{self.puesto}', "
            f"objetos={len(self.inventario)}"
            f")"
        )