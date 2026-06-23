class Simulador:

    def __init__(self):
        self.mesas = []
        self.empleados = []
        self.clientes = []
        self.estanterias = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_estanteria(self, estanteria):
        self.estanterias.append(estanteria)