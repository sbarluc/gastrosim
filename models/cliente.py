class Cliente:
    siguiente_id = 1

    def __init__(self, nombre, edad, specs=None):
        self.id = Cliente.siguiente_id
        Cliente.siguiente_id += 1

        self.nombre = nombre
        self.edad = edad
        self.specs = specs if specs is not None else []

        self.mesa_actual = None
        self.mesa_asignada = None
        self.sentado = False
    
    def asignar_mesa(self, mesa):
        self.mesa_asignada = mesa

    def agregar_spec(self, spec):
        self.specs.append(spec)

    def sentarse_en(self, mesa):
        if (not mesa.tiene_lugar()):
            return False
        mesa.ocupar_silla(self)
        self.sentado = True
        self.mesa_actual = mesa

    def pararse(self):
        self.mesa_actual.desocupar_silla(self)
        self.mesa_actual = None
        self.sentado = False

    def __repr__(self):
        specs = ", ".join(self.specs)
        return (
            f"      |Cliente[{self.id}] - {self.nombre}, {self.edad} años\n"
            f"      |specs: {self.specs}\n"
            f"      |mesa actual: {'-' if self.mesa_actual is None else (f'Mesa[{self.mesa_actual.id}]')}\n"
            f"      |mesa asignada: {'-' if self.mesa_asignada is None else (f'Mesa[{self.mesa_asignada.id}]')}\n"
            f"      |{'sentad@' if self.sentado else 'parad@'}\n"
        )