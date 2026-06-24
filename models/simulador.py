class Simulador:

    def __init__(self):
        self._mesas = []
        self._estanterias = []
        self._empleados = []
        self._clientes = []

        self._entidades = {}

    def agregar_mesas(self, mesas):
        for mesa in mesas:
            self._mesas.append(mesa)
            self._entidades[mesa.id_gral] = mesa
        return self

    def agregar_empleados(self, empleados):
        for empleado in empleados:
            self._empleados.append(empleado)
            self._entidades[empleado.id_gral] = empleado
        return self

    def agregar_clientes(self, clientes):
        for cliente in clientes:
            self._clientes.append(cliente)
            self._entidades[cliente.id_gral] = cliente
        return self

    def agregar_estanterias(self, estanterias):
        for estanteria in estanterias:
            self._estanterias.append(estanteria)
            self._entidades[estanteria.id_gral] = estanteria
        return self

    def buscar_entidad(self, id_gral):
        if id_gral not in self._entidades:
            return None
        return self._entidades[id_gral]
    
    def mostrar_universo(self):
        for mesa in self._mesas:
            salida = f"Mesa{mesa.id}" + \
            (f" <sentados: {mesa.clientes_sentados()}>" if mesa.esta_ocupada() else "") + \
            (f" <objetos: {mesa.objetos()}>" if len(mesa.objetos())>0 else "")
            print(salida)

        for estanteria in self._estanterias:
            print(f"Estanteria{estanteria.id}")

        for cliente in self._clientes:
            salida = f"Cliente{cliente.id} <nombre: {cliente.nombre}>" + \
            (f" <mesa actual: {cliente.mesa_actual()}>" if cliente.mesa_actual() is not None else "") + \
            (f" <mesa asignada: {cliente.mesa_asignada()}>" if cliente.mesa_asignada() is not None else "")
            print(salida)

        for empleado in self._empleados:
            print(f"Empleado{empleado.id} <nombre: {empleado.nombre}> <puesto: {empleado.puesto}>")
        
        