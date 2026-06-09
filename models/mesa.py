class Mesa:
    def __init__(self, id, capacidad_maxima):
        self.id = id
        self.capacidad_maxima = capacidad_maxima

        self.clientes = []
        self.objetos = []

        self.limpia = True

    def tiene_lugar(self):
        return len(self.clientes) < self.capacidad_maxima

    def esta_ocupada(self):
        return len(self.clientes) > 0
    
    def esta_limpia(self):
        return self.limpia

    def sentar_cliente(self, cliente):
        if not self.tiene_lugar():
            return False
        if cliente in self.clientes:
            return False

        self.clientes.append(cliente)

        cliente.mesa = self
        cliente.sentado = True

        return True
    
    def limpiar(self):
        self.limpia = True

    def ensuciar(self):
        self.limpia = False

    def cantidad_clientes(self):
        return len(self.clientes)

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            return objeto
        return None

    def agregar_objeto(self, objeto):
        return self.objetos.append(objeto)

    def __repr__(self):
        return (
            f"Mesa("
            f"id={self.id}, "
            f"clientes={self.cantidad_clientes()}/{self.capacidad_maxima}, "
            f"objetos={len(self.objetos)}, "
            f"estado={'limpia' if self.esta_limpia() else 'sucia'}"
            f")"
        )