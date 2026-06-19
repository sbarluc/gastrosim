class Mesa:
    siguiente_id = 1

    def __init__(self, id, sillas):
        self.id = Mesa.siguiente_id
        Mesa.siguiente_id += 1
        self.sillas = sillas

        self.clientes_sentados = []
        self.clientes = []
        self.objetos = []

        self.limpia = True

    def tiene_lugar(self):
        return len(self.clientes_sentados) < self.sillas

    def esta_ocupada(self):
        return len(self.clientes) > 0
    
    def esta_limpia(self):
        return self.limpia

    def asignar_cliente(self, cliente):
        self.clientes.append(cliente)
        return True
    
    def ocupar_silla(self, cliente):
        if not self.tiene_lugar():
            return False
        self.clientes_sentados.append(cliente)
        return True

    def desocupar_silla(self, cliente):
        if not cliente in self.clientes_sentados:
            return False
        self.clientes_sentados.remove(cliente)
        return True
    
    def limpiar(self):
        self.limpia = True

    def ensuciar(self):
        self.limpia = False

    def cantidad_clientes(self):
        return len(self.clientes)

    def cantidad_sentados(self):
        return self.clientes_sentados

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            return objeto
        return None

    def __repr__(self):
        return (
            f"      |Mesa[{self.id}] - {'limpia' if self.esta_limpia() else 'sucia'}\n"
            f"      |clientes: {[f'Cliente[{c.id}]' for c in self.clientes]}\n"
            f"      |sentados: {[f'Cliente[{c.id}]' for c in self.clientes_sentados]}\n" 
            f"      |objetos: (?/?) | {[o.nombre for o in self.objetos]}\n"
        )