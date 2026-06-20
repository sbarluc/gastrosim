class Entidad:
    siguiente_id = 1

    def __init__(self):
        self.id = Entidad.siguiente_id
        Entidad.siguiente_id += 1