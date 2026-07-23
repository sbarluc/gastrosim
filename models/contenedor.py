from models.entidad import Entidad
from models.posicion import Posicion

class Contenedor(Entidad):

    def __init__(self, tipo, objetos, carga_max, nombre=None):
        super().__init__(tipo, nombre=nombre)

        self._carga_actual = 0
        self._carga_max = carga_max

        self._objetos = []
        if objetos is not None: 
            self._objetos = objetos
            self._carga_actual = sum([objeto.peso for objeto in self._objetos])

        self.posicion = Posicion()

    def agregar_objeto(self, objeto):
        if objeto in self._objetos or not self.puede_cargar(objeto):
            return False
        self._objetos.append(objeto)
        self._carga_actual += objeto.peso
        return True

    def quitar_objeto(self, objeto):
        if objeto in self._objetos:
            self._objetos.remove(objeto)
            self._carga_actual -= objeto.peso
            return objeto
        
        return None
    
    def contiene(self, objeto):
        return objeto in self._objetos
    
    def cantidad_objetos(self):
        return len(self._objetos)
    
    def objetos(self):
        return self._objetos.copy()
    
    def obtener_objeto(self, nombre=None, id=None):
        for objeto in self._objetos:
            if id and objeto.id == id:
                return objeto
            if nombre and objeto.nombre == nombre:
                return objeto
        return None


    def puede_cargar(self, objeto):
        return self._carga_actual+objeto.peso <= self._carga_max
    
    def info(self):
        return (
            f"Objetos: {[o.info() for o in self._objetos]}"
        )