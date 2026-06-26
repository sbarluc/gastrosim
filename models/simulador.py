from models.tipo_entidad import TipoEntidad

class Simulador:

    def __init__(self):
        self._entidades = {
            TipoEntidad.MESA: {},
            TipoEntidad.EMPLEADO: {},
            TipoEntidad.CLIENTE: {},
            TipoEntidad.ESTANTERIA: {}
        }

    def agregar_mesas(self, mesas):
        for mesa in mesas:
            self._entidades[TipoEntidad.MESA][mesa.id] = mesa
        return self

    def agregar_empleados(self, empleados):
        for empleado in empleados:
            self._entidades[TipoEntidad.EMPLEADO][empleado.id] = empleado
        return self

    def agregar_clientes(self, clientes):
        for cliente in clientes:
            self._entidades[TipoEntidad.CLIENTE][cliente.id] = cliente
        return self

    def agregar_estanterias(self, estanterias):
        for estanteria in estanterias:
            self._entidades[TipoEntidad.ESTANTERIA][estanteria.id] = estanteria
        return self

    def buscar_entidad(self, id_gral):
        if id_gral not in self._entidades:
            return None
        return self._entidades[id_gral]
    
    def mostrar_universo(self):
        for id_mesa, mesa in self._entidades[TipoEntidad.MESA].items():
            print(f"MESA {id_mesa}" + \
            (f" <sentados: {mesa.clientes_sentados()}>" if mesa.esta_ocupada() else "") + \
            (f" <objetos: {mesa.objetos()}>" if len(mesa.objetos())>0 else ""))

        for id_cliente, cliente in self._entidades[TipoEntidad.CLIENTE].items():
            print(f"CLIENTE {id_cliente} <nombre: {cliente.nombre}>" + \
            (f" <mesa asignada: {cliente.mesa_asignada()}>" if cliente.mesa_asignada() is not None else "") + \
            (f" <sentad@ en: {cliente.mesa_actual()}>" if cliente.mesa_actual() is not None else ""))

        for id_empleado, empleado in self._entidades[TipoEntidad.EMPLEADO].items():
            print(f"EMPLEADO {id_empleado}" + \
            (f" <nombre: {empleado.nombre}> <puesto: {empleado.puesto}>") + \
            (f" <objetos: {empleado.inventario().objetos()}>" if len(empleado.inventario().objetos())>0 else ""))
            
        for id_estanteria, estanteria in self._entidades[TipoEntidad.ESTANTERIA].items():
            print(f"ESTANTERIA {id_estanteria}" + \
            (f" <objetos: {estanteria.objetos()}>" if len(estanteria.objetos())>0 else ""))
        