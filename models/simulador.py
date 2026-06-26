class Simulador:

    def __init__(self):
        self._entidades = {
            "mesa": {},
            "empleado": {},
            "cliente": {},
            "estanteria": {}
        }

    def agregar_mesas(self, mesas):
        for mesa in mesas:
            self._entidades["mesa"][mesa.id] = mesa
        return self

    def agregar_empleados(self, empleados):
        for empleado in empleados:
            self._entidades["empleado"][empleado.id] = empleado
        return self

    def agregar_clientes(self, clientes):
        for cliente in clientes:
            self._entidades["cliente"][cliente.id] = cliente
        return self

    def agregar_estanterias(self, estanterias):
        for estanteria in estanterias:
            self._entidades["estanteria"][estanteria.id] = estanteria
        return self

    def buscar_entidad(self, id_gral):
        if id_gral not in self._entidades:
            return None
        return self._entidades[id_gral]
    
    def mostrar_universo(self):
        for id_mesa, mesa in self._entidades["mesa"].items():
            print(f"Mesa{id_mesa}" + \
            (f" <sentados: {mesa.clientes_sentados()}>" if mesa.esta_ocupada() else "") + \
            (f" <objetos: {mesa.objetos()}>" if len(mesa.objetos())>0 else ""))

        for id_cliente, cliente in self._entidades["cliente"].items():
            print(f"Cliente{id_cliente} <nombre: {cliente.nombre}>" + \
            (f" <mesa asignada: {cliente.mesa_asignada()}>" if cliente.mesa_asignada() is not None else "") + \
            (f" <sentad@ en: {cliente.mesa_actual()}>" if cliente.mesa_actual() is not None else ""))

        for id_empleado, empleado in self._entidades["empleado"].items():
            print(f"Empleado{id_empleado}" + \
            (f" <nombre: {empleado.nombre}> <puesto: {empleado.puesto}>") + \
            (f" <objetos: {empleado.inventario().objetos()}>" if len(empleado.inventario().objetos())>0 else ""))
            
        for id_estanteria, estanteria in self._entidades["estanteria"].items():
            print(f"Estanteria{id_estanteria}" + \
            (f" <objetos: {estanteria.objetos()}>" if len(estanteria.objetos())>0 else ""))
        