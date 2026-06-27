class Entidad:
    siguiente_id = 1

    def __init__(self, tipo):
        self.tipo = tipo
        self.id = self.__class__.siguiente_id
        self.__class__.siguiente_id += 1