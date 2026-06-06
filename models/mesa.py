class Mesa:
    def __init__(self, id, capacidad_maxima):
        self.id = id
        self.capacidad_maxima = capacidad_maxima

        self.clientes = []
        self.objetos = []