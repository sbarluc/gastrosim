class Cliente:
    siguiente_id = 1

    def __init__(self, nombre, edad):
        self.id = Cliente.siguiente_id
        Cliente.siguiente_id += 1

        self.nombre = nombre
        self.edad = edad
        self.caracteristicas = []

        self.mesa = None
        self.sentado = False
    
    def agregar_caracteristica(self, caracteristica):
        self.caracteristicas.append(caracteristica)

    def sentarse(self, mesa):
        if (not mesa.tiene_lugar()):
            return False
        

    def pararse(self):
        self.sentado = False

    def __repr__(self):
        caracteristicas = ", ".join(self.caracteristicas)
        return (
            f"Cliente("
            f"id={self.id}, "
            f"nombre={self.nombre}, "
            f"edad={self.edad}"
            f"{', ' + caracteristicas if caracteristicas else ''}, "
            f"{'sentad@' if self.sentado else 'parad@'}"
            f")"
        )