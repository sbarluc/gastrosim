from models.entidad import Entidad

class Contenedor(Entidad):

    def __init__(self, tipo, objetos=None, nombre="", carga_max=float("inf")):
        super().__init__(tipo)

        self.nombre = nombre
        self._carga_actual = 0
        self._carga_max = carga_max

        self._objetos = []
        if objetos is not None: 
            self._objetos = objetos
            self._carga_actual = sum([objeto.peso for objeto in self._objetos])

    def agregar_objeto(self, objeto):
        if objeto in self._objetos or \
            not self.puede_cargar(objeto):
            return False
        self._objetos.append(objeto)
        return True

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
    
    def puede_cargar(self, objeto):
        return self._carga_actual+objeto.peso <= self._carga_max