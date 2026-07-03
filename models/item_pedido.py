from models.entidad import Entidad

class ItemPedido(Entidad):

    def __init__(self, nombre="", valor=0):
        self.nombre = nombre
        self._valor = valor
        self._estados = set()

#------------------------------------------------------------------------------------

    def valor(self):
        return self._valor
    
    def preparar_para_pedir(self):
        return self._estados.add("PARA_PEDIR")
    
    def esta_para_pedir(self):
        return "PARA_PEDIR" in self._estados
    
    def pedir(self):
        return self._estados.add("ESPERANDO")

    def fue_pedido(self):
        return "ESPERANDO" in self._estados
    
#-------------------------------------------------------------------------------------
    
    def entregar(self):
        return self._estados.add("ENTREGADO")
    
    def fue_entregado(self):
        return "ENTREGADO" in self._estados

#-------------------------------------------------------------------------------------

    @classmethod
    def desde_menu(cls, menu, nombre):
        precio = menu.precio(nombre)
        if precio is None:
            return None
        return cls(nombre, precio)