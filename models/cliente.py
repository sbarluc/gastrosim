class Cliente:
    siguiente_id = 1

    def __init__(self, nombre, edad):
        self.id = Cliente.siguiente_id
        Cliente.siguiente_id += 1

        self.nombre = nombre
        self.edad = edad

        self.mesa = None
        self.sentado = False