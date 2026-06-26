from models.entidad import Entidad

class Contenedor(Entidad):

    def __init__(self, objetos=None, nombre=""):
        super().__init__()

        self.nombre = nombre

        self._objetos = objetos if objetos is not None else []

    def agregar_objeto(self, objeto):
        self._objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self._objetos:
            self._objetos.remove(objeto)
            return objeto
        
        return None
    
    def contiene(self, objeto):
        return objeto in self._objetos
    
    def cantidad_objetos(self):
        return len(self._objetos)
    
    def objetos(self):
        return self._objetos.copy()