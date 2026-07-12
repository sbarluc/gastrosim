class Entidad:
    siguiente_id = 1

    def __init__(self, tipo, nombre=None):
        self.tipo = tipo
        self.id = self.__class__.siguiente_id
        self.__class__.siguiente_id += 1
        self.nombre = nombre if nombre else ""
    
    def __repr__(self):
        return f"<{self.id}|{self.tipo.name}{f':{self.nombre}' if self.nombre else ''}>"