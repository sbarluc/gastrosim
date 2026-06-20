class Objeto:
    siguiente_id = 1

    def __init__(self, nombre):
        self.nombre = nombre
        self.id = Objeto.siguiente_id

    def __repr__(self):
        return (
            f"      |Objeto[{self.id}] - {self.nombre}\n"
        )