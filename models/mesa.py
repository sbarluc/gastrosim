class Mesa:
    def __init__(self, id, capacidad_maxima):
        self.id = id
        self.capacidad_maxima = capacidad_maxima

        self.clientes = []
        self.objetos = []

    def tiene_lugar(self):
        return len(self.clientes) < self.capacidad_maxima

    def sentar_cliente(self, cliente):
        if not self.tiene_lugar():
            return False
        if cliente in self.clientes:
            return False

        self.clientes.append(cliente)

        cliente.mesa = self
        cliente.sentado = True

        return True

    def __repr__(self):
        return (
            f"Mesa(id={self.id}, "
            f"clientes={len(self.clientes)}/{self.capacidad_maxima}, "
            f"objetos={len(self.objetos)})"
        )