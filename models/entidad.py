class Entidad:
    siguiente_id = 1
    siguiente_id_gral = 1

    def __init__(self, tipo):
        self.tipo = tipo

        self.id = self.__class__.siguiente_id
        self.__class__.siguiente_id += 1
        
        self.id_gral = Entidad.siguiente_id_gral
        Entidad.siguiente_id_gral += 1