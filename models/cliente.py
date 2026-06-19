class Cliente:
    siguiente_id = 1

    def __init__(self, nombre, edad, specs=[]):
        self.id = Cliente.siguiente_id
        Cliente.siguiente_id += 1

        self.nombre = nombre
        self.edad = edad
        self.specs = specs

        self.mesa = None
        self.sentado = False
    
    def agregar_spec(self, spec):
        self.specs.append(spec)

    def sentarse_en(self, mesa):
        if (not mesa.tiene_lugar()):
            return False
        mesa.ocupar_silla(self)
        self.sentado = True
        self.mesa = mesa

    def pararse(self):
        self.mesa.desocupar_silla(self)
        self.sentado = False

    def __repr__(self):
        specs = ", ".join(self.specs)
        return (
            f"      |Cliente[{self.id}] - {self.nombre}, {self.edad} años\n"
            f"      |specs: {self.specs}\n"
            f"      |{'sentad@' if self.sentado else 'parad@'}\n"
        )