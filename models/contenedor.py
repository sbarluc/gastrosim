class Contenedor:

    def __init__(self, objetos=None, nombre=""):
        self.nombre = nombre
        self.objetos = objetos if objetos is not None else []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            return objeto
        return None
    
    def contiene(self, objeto):
        return objeto in self.objetos
    
    def cantidad_objetos(self):
        return len(self.objetos)